from abc import abstractmethod, ABC


class IBaseDevice(ABC):
    @abstractmethod
    def get_id(self):
        """
        Get the unique device ID
        :return: str
        """
        raise NotImplementedError

    @abstractmethod
    def get_state(self) -> dict:
        """
        Get the current device state
        :return: dict of 'text' holding human-readable device state and 'data' holding custom device state data
        """
        raise NotImplementedError

    @abstractmethod
    def set_state(self, state) -> None:
        """
        Set the device state
        :param state: customer device state data
        :return: None
        """
        raise NotImplementedError

    @abstractmethod
    def get_registration_data(self) -> dict:
        """
        Get the device registration data
        :return: dict of 'config' holding device configuration data
        and 'state' holding device state from get_state() method
        """
        raise NotImplementedError

    @abstractmethod
    def get_pairing_code(self):
        raise NotImplementedError

    @abstractmethod
    def handle_pairing_update(self, update):
        raise NotImplementedError