import json
from typing import List

from .base_ser import BaseSerializer
from personal_data_manager.models.personal_data import PersonalData


class JSONSerializer(BaseSerializer):
    """
    A serializer for converting PersonalData objects to and from JSON format.
    """

    def serialize(self, records: List[PersonalData]) -> str:
        """
        Serialize a list of PersonalData objects to JSON format.

        Args:
            records (List[PersonalData]): A list of PersonalData objects.

        Returns:
            str: Serialized records in JSON format.

        Raises:
            ValueError: If no records are found to serialize.
        """
        # Call the base class implementation
        super().serialize(records)

        # Convert each PersonalData object to a dictionary and store in a list
        json_data = []
        for record in records:
            json_data.append(record.to_dict())

        # Convert the list of dictionaries to a JSON string
        return json.dumps(json_data)

    def deserialize(self, serialized_records: str) -> List[PersonalData]:
        """
        Deserialize records from a JSON format.

        Args:
            serialized_records (str): Serialized records in JSON format.

        Returns:
            List[PersonalData]: A list of deserialized PersonalData objects.

        Raises:
            ValueError: If no records are found to deserialize or if the input data is not valid JSON format.
        """
        # Call the base class implementation
        super().deserialize(serialized_records)

        # Attempt to create a list of dictionaries from the serialized_records
        try:
            json_data = json.loads(serialized_records)
        except json.JSONDecodeError as e:
            # Raise an error if the input data is not valid JSON format
            raise ValueError(f"Invalid JSON data: {e}")

        records = []

        # Read each dictionary from the json_data list
        for record_data in json_data:
            try:
                # Extract each field from the dictionary and create a new PersonalData object
                name = record_data["name"]
                address = record_data["address"]
                phone_number = record_data["phone_number"]
                records.append(PersonalData(name, address, phone_number))
            except KeyError as e:
                # Raise an error if any required field is missing from the record_data
                raise ValueError(f"Missing required field: {e}")

        # Return the list of PersonalData objects
        return records
