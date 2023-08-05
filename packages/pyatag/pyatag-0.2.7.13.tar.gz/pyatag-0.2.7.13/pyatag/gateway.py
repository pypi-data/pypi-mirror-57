"""Gateway connecting to ATAG thermostat."""
import logging
import aiohttp

from .helpers import HostData, HttpConnector, get_data_from_jsonreply, check_reply
from .errors import ResponseError, RequestError

_LOGGER = logging.getLogger(__name__)
SESSION = 'session'
HOST = 'host'
PORT = 'port'
MAIL = 'mail'
INTERFACE = 'interface'
DEVICE = 'device'


class AtagDataStore:
    """Central data store entity."""

    def __init__(
            self, session=None, host=None, port=None,
            mail=None, interface=None):

        self.initialized = False
        self.paired = False
        self.session = session
        self._connector = None
        # TODO: overlap met HostData eruit slopen // simpeler maken // self.session ?
        self.host_config = {
            HOST: host,
            PORT: port,
            MAIL: mail,
            INTERFACE: interface,
            DEVICE: None
        }
        self.host_data = None
        self.sensordata = {}

    async def async_finalize_init(self):
        """Atag Discovery in case no host provided."""
        if self.host_config[HOST] is None:
            from .discovery import discover_atag
            try:
                _LOGGER.debug("No host provided, attempting discovery...")
                host, device = await discover_atag()
                self.host_config[HOST] = host
                self.host_config[DEVICE] = device
            except RequestError:
                _LOGGER.error("Atag host discovery failed")
                return False
            _LOGGER.debug("Found Atag at %s\nDevice id: %s", host, device)
        if self.host_config[INTERFACE] is None:
            import netifaces
            self.host_config[INTERFACE] = netifaces.gateways()[
                'default'][netifaces.AF_INET][1]
        try:
            self.host_data = HostData(self.host_config)
        except RequestError:
            _LOGGER.error(
                "Initialization failed: Incorrect host data provided!")
        if self.session is None:
            self.session = aiohttp.ClientSession()
        if type(self.session).__name__ == 'ClientSession':
            self._connector = HttpConnector(self.host_data, self.session)
        else:
            _LOGGER.error("Not a valid session: %s",
                          type(self.session).__name__)
        self.initialized = True

    async def async_update(self):
        """Read data from thermostat."""
        if not self.paired:
            _LOGGER.debug("Atag not paired yet - attempting..")
            if not await self.async_check_pair_status():
                _LOGGER.error(
                    "Pairing failed - please confirm pairing on device")
                return
        try:
            json_data = await self._connector.atag_put(data=self.host_data.retrieve_msg)
            sensordata = get_data_from_jsonreply(json_data)
            if sensordata:
                self.sensordata = sensordata
        except ResponseError as err:
            _LOGGER.warning(
                'Atag sensor failed to update:\nResponse:   %s', err)

    async def async_set_atag(self, **kwargs):
        """set mode and/or temperature."""

        json_payload = self.host_data.get_update_msg(**kwargs)
        try:
            json_data = await self._connector.atag_put(data=json_payload)
            _LOGGER.debug("Update reply: %s", json_data)
            if not check_reply(json_data):
                raise ResponseError("Invalid reply from Atag: {}".format(json_data))
        except (ResponseError, KeyError) as err:
            _LOGGER.error("Failed to set Atag: %s", err)
            return False

    async def async_check_pair_status(self):
        """Confirm we are authorized."""

        if self.paired:
            return True
        if not self.initialized:
            await self.async_finalize_init()
            if not self.initialized:
                return False
        try:
            json_data = await self._connector.atag_put(data=self.host_data.pair_msg)
            status = check_reply(json_data)
        except ResponseError as err:
            _LOGGER.error("Pairing failed\nPairmsg: %s\nError: %s", self.host_data.pair_msg, err)
            return False
        if status == 2:
            self.paired = True
            _LOGGER.debug("AtagDataStore paired")
            return True
        if status == 1:
            _LOGGER.warning("Waiting for pairing confirmation")
        elif status == 3:
            _LOGGER.warning("Waiting for pairing confirmation")
        elif status == 0:
            _LOGGER.warning("No status returned from ATAG One")
        _LOGGER.warning("Atag not paired!\n%s", json_data)
        return False

    async def async_close(self):
        """Close the connection"""
        await self._connector.async_close()
