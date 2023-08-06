import logging as _logging
import time
from threading import Event, Thread

import paho.mqtt.client as _mqtt
from ..proto import device_pb2 as _device, common_pb2 as _common
from ..proto.device_pb2 import Config as RegistrationData
from ..proto import states_pb2 as DeviceStates
from ..proto import types_pb2 as DeviceTypes
from ..proto import capabilities_pb2 as DeviceCapabilities
from .crypto import Crypto as _Crypto
from .device_protocols import IBaseDevice as _IBaseDevice
from .errors import DeviceNotSetException as _DeviceNotSetException, KeysNotSetException as _KeysNotSetException

__all__ = [
    "LightberryClient",
    "RegistrationData",
    "DeviceStates",
    "DeviceTypes",
    "DeviceCapabilities"
]

HEARTBEAT_INTERVAL = 30


class LightberryClient:
    def __init__(self, broker: str, port: int) -> None:
        """
        Creates new instance of LightberryClient helper
        :param broker: domain name of MQTT broker
        :type broker: str
        :param port: port of MQTT broker
        :type port: int
        """
        self._logger = _logging.getLogger(__name__)
        self._broker = broker
        self._port = port

        self._device = None
        self._crypto: _Crypto = None
        self._mqttc = None
        self._heartbeat_exit_event = Event()
        self._heartbeat_thread = Thread(target=self._heartbeat_loop)

    def set_secret(self, secret: str) -> None:
        self._crypto = _Crypto(secret)

    def set_device(self, device_inst: _IBaseDevice) -> None:
        self._device = device_inst

    def connect(self) -> None:
        """
        Connects to the MQTT broker and initiates client connection
        :return: None
        """
        # Are we ready to connect?
        if not isinstance(self._device, _IBaseDevice):
            raise _DeviceNotSetException
        if type(self._crypto) is not _Crypto:
            raise _KeysNotSetException('Signing key not set')

        # Setup MQTT client
        self._mqttc = _mqtt.Client(client_id=self._device.get_id())
        self._mqttc.on_connect = self._handle_connect
        self._mqttc.on_disconnect = self._handle_disconnect

        # Add Basic MQTT callbacks
        device_id = self._device.get_id()
        self._mqttc.message_callback_add('to/{}/state'.format(device_id), self._handle_state_update)
        # self._mqttc.message_callback_add('to/{}/pairing'.format(device_id), self._handle_pairing_update)
        self._mqttc.message_callback_add('host/online', self._handle_host_ping)

        # Initiate MQTT connection to broker
        self._mqttc.connect(self._broker, self._port, 10)
        try:
            self._heartbeat_thread.start()
            self._mqttc.loop_forever()
        finally:
            self._heartbeat_exit_event.set()
            self._heartbeat_thread.join(5)

    def disconnect(self) -> None:
        """
        Disconnects from the MQTT broker
        :return: None
        """
        # End MQTT connection
        self._mqttc.loop_stop()
        self._mqttc.disconnect()

    def _heartbeat_loop(self):
        while not self._heartbeat_exit_event.wait(HEARTBEAT_INTERVAL):
            hb = _common.Heartbeat()
            hb.id = self._device.get_id()
            hb.timestamp = int(time.time())
            message = hb.SerializeToString()
            data = self._crypto.encrypt(message)
            self._mqttc.publish("from/{}/heartbeat".format(self._device.get_id()), data)

    # Publishers
    def _publish_registration(self):
        self._logger.info('Registering with host')
        self._mqttc.subscribe('host/+', 0)
        self._mqttc.subscribe('to/{}/+'.format(self._device.get_id()), 0)

        config = self._device.get_registration_data()
        message = config.SerializeToString()
        data = self._crypto.encrypt(message)
        self._mqttc.publish("from/{}/online".format(self._device.get_id()), data)

        self._publish_state()
        self._logger.info('Registration complete!')

        self._publish_pairing_code()

    def _publish_pairing_code(self):
        self._logger.info('Publishing pairing code')
        message = _device.PairingUpdate()
        message.id = self._device.get_id()
        message.timestamp = int(time.time())
        message.code = self._device.get_pairing_code()
        message = message.SerializeToString()
        data = self._crypto.encrypt(message)
        self._mqttc.publish("from/{}/pairing".format(self._device.get_id()), data)

    def _publish_state(self):
        self._logger.debug('Publishing state')
        state = self._device.get_state()
        update = _device.StateUpdate()
        update.id = self._device.get_id()
        update.state.Pack(state)
        update.timestamp = int(time.time())
        message = update.SerializeToString()
        data = self._crypto.encrypt(message)
        self._mqttc.publish("from/{}/state".format(self._device.get_id()), data)

    # Message Handlers
    def _handle_connect(self, mqttc, obj, flags, rc):
        self._logger.info(f'Connected to broker {self._broker}')
        self._publish_registration()

    def _handle_disconnect(self, client, user_data, rc):
        self._logger.info('Disconnected from broker')
        self._heartbeat_timer.cancel()

    def _handle_state_update(self, mqttc, obj, msg):
        self._logger.info('Received state update')
        message = self._crypto.decrypt(msg.payload)
        state_update = _device.StateUpdate.FromString(message)
        if state_update.id == self._device.get_id():
            self._logger.debug('Received state {}'.format(state_update))
            state = state_update.state.Unpack()
            self._device.set_state(state)
            # TODO: proactive reporting to Alexa
            self._publish_state()
        else:
            self._logger.warning('State could not be decrypted')

    def _handle_host_ping(self, mqttc, obj, msg):
        self._logger.info('Host came online')
        self._publish_registration()
