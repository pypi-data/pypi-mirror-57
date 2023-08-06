import logging.config

from device import Device
from lightberry import LightberryClient

deviceId = "5df2af0e148d96fee75ca3d8"
secret = "RAlXpI7M+Wo/cSNIV74Xzw=="

device = Device(deviceId)

client = LightberryClient("localhost", 1883)

client.set_device(device)
client.set_secret(secret)
client.connect()
