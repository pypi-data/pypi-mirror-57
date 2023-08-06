# LightBerry Client Library
Lightberry is an open source home automation platform with Alexa integration. This library allows the easy development
of a client implementation in the Python language.

## Installation  
To install the Lightberry client library, run the following command from a terminal:  
```pip3 install lightberry-lib```

## Usage  
```
from lightberrylib import LightberryClient

device = Device(config.deviceId, config.deviceConfig)

client = LightberryClient(config.mqtt.host, config.mqtt.port)
client.set_device(device)
client.set_secret(<SECRET>)
client.connect()
```
The `LightberryClient` constructor accepts two arguments: the MQTT host address and the port (typically 1883).  
The `Device` class is a custom class which is unique to your implmentation. It must implement the 
`lightberry-lib.device_protocols.IBaseDevice` protocol, and optionally the 
`lightberry-lib.device_protocols.IAlexaEnabledDevice` protocol to enable Alexa functionality.   
The keys passed to the `client.set_keys()` method are obtained from the Lightberry API through the 
`POST /api/developer/devices` endpoint.  

For more information, check out the reference implementations in the `examples` directory.