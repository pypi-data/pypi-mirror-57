import logging
import time
from enum import IntEnum

from lightberry.device_protocols import IBaseDevice
from lightberry import DeviceTypes, DeviceCapabilities, DeviceStates, RegistrationData


def get_utc_timestamp(seconds=None):
    return time.strftime("%Y-%m-%dT%H:%M:%S.00Z", time.gmtime(seconds))


class Device(IBaseDevice):
    def __init__(self, device_id):
        self._id = device_id
        self._state = DeviceStates.SWITCH(state=DeviceStates.SWITCH.OFF)

    def get_id(self):
        return self._id

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state
        logging.info('Setting state to {}'.format(state))

    def get_registration_data(self):
        config = RegistrationData()
        config.id = self._id
        config.manufacturer = "Lightberry"
        config.model = "Dummy Switch"
        config.primaryType = DeviceTypes.SWITCH
        config.capabilities.append(DeviceCapabilities.ONOFF)
        return config

    def get_pairing_code(self):
        return "DUMMY"

    def handle_pairing_update(self, update):
        pass


