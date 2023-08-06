from json import dumps, loads
import logging
from base64 import b64decode

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad


class Crypto:
    def __init__(self, secret):
        if type(secret) is str:
            secret = b64decode(secret)
        self.secret = secret
        self.__logger__ = logging.getLogger('lightberry_lib')

    def decrypt(self, data):
        iv = data[:AES.block_size]
        data = data[AES.block_size:]
        cipher = AES.new(self.secret, AES.MODE_CBC, iv=iv)
        try:
            message = cipher.decrypt(data)
            message = unpad(message, AES.block_size)
            self.__logger__.debug('Decrypted message')
            return message
        except ValueError:
            self.__logger__.warning('Decryption failed')
            return None

    def encrypt(self, message):
        self.__logger__.info('Encrypting message')
        cipher = AES.new(self.secret, AES.MODE_CBC)
        message = pad(message, AES.block_size)
        message = cipher.encrypt(message)
        return cipher.iv + message
