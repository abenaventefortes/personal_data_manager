import re


class PersonalData:
    """
    A class to represent a personal data record.

    Attributes:
        name (str): The name of the person.
        address (str): The address of the person.
        phone_number (str): The phone number of the person.
    """

    def __init__(self, name: str, address: str, phone_number: str) -> None:
        """Initializes a PersonalData object with the provided attributes.

        Args:
            name (str): The name of the person.
            address (str): The address of the person.
            phone_number (str): The phone number of the person.

        Raises:
            ValueError: If any of the attributes are empty or None, or if the phone number
                        is not in the format ###-###-####.
            TypeError: If any of the attributes are not strings.
        """
        # Check if the attributes are of the correct type
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(address, str):
            raise TypeError("Address must be a string")
        if not isinstance(phone_number, str):
            raise TypeError("Phone number must be a string")

        # Check if the attributes are not empty
        if not name:
            raise ValueError("Name cannot be empty")
        if not address:
            raise ValueError("Address cannot be empty")
        if not phone_number:
            raise ValueError("Phone number cannot be empty")

        # Check if the phone number is in the correct format
        if not re.match(r"^\d{3}-\d{3}-\d{4}$", phone_number):
            raise ValueError("Phone number must be in the format ###-###-####")

        # Set the attributes
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def __repr__(self) -> str:
        """Returns a string representation of the PersonalData object.

        Returns:
            str: A string representation of the PersonalData object.
        """
        return f"{self.name}, {self.address}, {self.phone_number}"

    def to_dict(self) -> dict:
        """Converts the PersonalData object to a dictionary.

        Returns:
            dict: A dictionary representation of the PersonalData object.
        """
        return {
            "name": self.name,
            "address": self.address,
            "phone_number": self.phone_number,
        }
