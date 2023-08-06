import logging
import time

from lightberry.device_protocols import IBaseDevice, IAlexaEnabledDevice


def get_utc_timestamp(seconds=None):
    return time.strftime("%Y-%m-%dT%H:%M:%S.00Z", time.gmtime(seconds))


class Controller:
    def __init__(self):
        self.setpoint = 72
        self.temp = 68

    def get_state(self):
        return {
            'setpoint': self.setpoint,
            'temp': self.temp
        }

    def get_mode(self):
        if self.setpoint < self.temp - 2:
            return 'HEAT'
        elif self.setpoint > self.temp + 2:
            return 'COOL'
        else:
            return 'AUTO'


class Device(IBaseDevice, IAlexaEnabledDevice):
    def __init__(self, device_id, config):
        self.__device_id__ = device_id
        self.__config__ = config
        self.__controller__ = Controller()

        print('Pairing code: {}'.format(self.__config__.get('pairingCode')))

    def get_id(self):
        return self.__device_id__

    def get_state(self):
        return {
            'data': self.__controller__.setpoint,
            'text': F'{self.__controller__.get_state()["setpoint"]} degrees F',
            'alexa': [
                {
                    "namespace": "Alexa.ThermostatController",
                    "name": "targetSetpoint",
                    "value": {
                        "value": self.__controller__.setpoint,
                        "scale": "FAHRENHEIT"
                    },
                    "timeOfSample": get_utc_timestamp(),
                    "uncertaintyInMilliseconds": 500
                },
                {
                    "namespace": "Alexa.ThermostatController",
                    "name": "thermostatMode",
                    "value": self.__controller__.get_mode(),
                    "timeOfSample": get_utc_timestamp(),
                    "uncertaintyInMilliseconds": 500
                },
                {
                    "namespace": "Alexa.TemperatureSensor",
                    "name": "temperature",
                    "value": {
                        "value": self.__controller__.temp,
                        "scale": "FAHRENHEIT"
                    },
                    "timeOfSample": get_utc_timestamp(),
                    "uncertaintyInMilliseconds": 1000
                }
            ]
        }

    def set_state(self, state):
        self.__controller__.setpoint = int(state)
        logging.info('Setting state to {}'.format(self.get_state().get('text')))
        # TODO: proactively report state to Alexa

    def get_registration_data(self):
        return {
            'config': self.__config__,
            'state': self.get_state(),
        }

    def handle_alexa(self, request):
        logging.info('Alexa request received')
        logging.debug(request)

        if request['directive']['header']['namespace'] == 'Alexa.ThermostatController':
            if request['directive']['header']['name'] == 'SetTargetTemperature':
                if request['directive']['payload']['targetSetpoint']:
                    if request['directive']['payload']['targetSetpoint']['scale'] == 'FAHRENHEIT':
                        self.set_state(request['directive']['payload']['targetSetpoint']['value'])
