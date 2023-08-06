import logging.config

import config
from device import Device
from lightberry import LightberryClient

logging.config.dictConfig(config.logging)

device = Device(config.deviceId, config.deviceConfig)

client = LightberryClient(config.mqtt.host, config.mqtt.port)
client.set_device(device)
client.set_keys(config.deviceId, config.secret)
client.connect()
