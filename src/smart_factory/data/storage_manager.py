from typing import Optional


class StorageManager:
    """ Class to manage the data storage of IoT Data """

    def __init__(self):
        """ Initialize the data manager with an empty dictionary to store sensor and actuator data """
        self.device_description_dict = {}
        self.device_status_dict = {}

    def store_device_description(self, device_id: str, device_description: str) -> None:
        """ Store a new device description """
        self.device_description_dict[device_id] = device_description

    def remove_device_description(self, device_id: str) -> None:
        """ Remove a stored device description """
        if device_id in self.device_description_dict.keys():
            del self.device_status_dict[device_id]

    def get_device_description(self, device_id: str) -> Optional[str]:
        """ Get a device description by its ID """
        if device_id in self.device_description_dict.keys():
                return self.device_description_dict[device_id]
        else:
            return None

    def get_all_devices_description(self) -> dict[str, str]:
        """ Return all the device Descriptions """
        return self.device_description_dict

    def store_device_status(self, device_id: str, status: str) -> None:
        """ Store a status for a devices. It can be associated both a variation of a
        Sensor or a status change in an actuator """
        if device_id not in self.device_status_dict:
            self.device_status_dict[device_id] = []
        self.device_status_dict[device_id].append(status)

    def get_singol_device_status(self, device_id) -> list[str]:
        """ Get all the status up to this moment for a specific devices """
        return self.device_status_dict.get(device_id, [])

    # Get all status for all devices
    def get_all_devices_status(self) -> dict[str, list[str]]:
        """ Get all status for all devices """
        return self.device_status_dict


