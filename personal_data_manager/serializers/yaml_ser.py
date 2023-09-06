import yaml
from typing import List

from .base_ser import BaseSerializer
from personal_data_manager.models.personal_data import PersonalData


class YAMLSerializer(BaseSerializer):
    """
    A serializer for converting PersonalData objects to and from YAML format.
    """

    def serialize(self, records: List[PersonalData]) -> str:
        """
        Serialize a list of PersonalData objects to YAML format.

        Args:
            records (List[PersonalData]): A list of PersonalData objects.

        Returns:
            str: Serialized records in YAML format.

        Raises:
            ValueError: If no records are found to serialize.
        """
        # Call the base class implementation
        super().serialize(records)

        # Create an empty list
        yaml_data = []

        # Loop through each record in the input list
        for record in records:
            # Convert the record to a dictionary and add it to the list
            yaml_data.append(record.__dict__)

        # Serialize the list of dictionaries to YAML format
        return yaml.dump(yaml_data)

    def deserialize(self, serialized_records: str) -> List[PersonalData]:
        """
        Deserialize records from a YAML format.

        Args:
            serialized_records (str): Serialized records in YAML format.

        Returns:
            List[PersonalData]: A list of deserialized PersonalData objects.

        Raises:
            ValueError: If no records are found to deserialize or if the input data is not valid YAML format.
        """
        # Call the base class implementation
        super().deserialize(serialized_records)

        try:
            # Deserialize the YAML string into a list of dictionaries
            yaml_data = yaml.safe_load(serialized_records)
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML data: {e}")

        # Convert the dictionaries to PersonalData objects
        records = []
        for record_data in yaml_data:
            try:
                # Create a new PersonalData object from the dictionary data
                personal_data = PersonalData(
                    name=record_data['name'],
                    address=record_data['address'],
                    phone_number=record_data['phone_number']
                )
                # Append the new PersonalData object to the list of records
                records.append(personal_data)
            except KeyError as e:
                raise ValueError(f"Missing required field: {e}")

        # Return the list of PersonalData objects
        return records
