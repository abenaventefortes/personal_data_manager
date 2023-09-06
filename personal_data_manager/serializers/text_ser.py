from typing import List

from .base_ser import BaseSerializer
from personal_data_manager.models.personal_data import PersonalData


class TextSerializer(BaseSerializer):
    """
    A class to represent a text serializer.
    """

    def serialize(self, records: List[PersonalData]) -> str:
        """
        Serialize a list of PersonalData objects to a plain text format.

        Args:
            records (List[PersonalData]): A list of PersonalData objects.

        Returns:
            str: Serialized records in plain text format.

        Raises:
            ValueError: If no records are found to serialize.
        """
        # Call the base class implementation
        super().serialize(records)

        output = ""
        # Loop through each record and append the record information to the output string
        for record in records:
            output += f"{record.name},{record.address},{record.phone_number}\n"
        return output

    def deserialize(self, serialized_records: str) -> list:
        """
        Deserialize records from a plain text format.

        Args:
            serialized_records (str): Serialized records in plain text format.

        Returns:
            list: A list of deserialized PersonalData objects.

        Raises:
            ValueError: If no records are found to deserialize or if the input data is not in the expected format.
        """
        # Call the base class implementation
        super().deserialize(serialized_records)

        records = []
        # Split serialized data into lines and loop through each line
        for line in serialized_records.strip().split("\n"):
            # Split line into components
            components = line.strip().split(",")
            # Ensure that there are exactly three components
            if len(components) != 3:
                raise ValueError("Invalid data format.")
            # Create a PersonalData object from the components and add it to the list
            record = PersonalData(components[0], components[1], components[2])
            records.append(record)

        return records
