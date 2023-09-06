import csv
from io import StringIO
from typing import List

from .base_ser import BaseSerializer
from personal_data_manager.models.personal_data import PersonalData


class CSVSerializer(BaseSerializer):
    """
    A serializer for converting PersonalData objects to and from CSV format.
    """

    def serialize(self, records: List[PersonalData]) -> str:
        """
        Serialize a list of PersonalData objects to CSV format.

        Args:
            records (List[PersonalData]): A list of PersonalData objects.

        Returns:
            str: Serialized records in CSV format.

        Raises:
            ValueError: If no records are found to serialize.
        """
        # Call the base class implementation
        super().serialize(records)

        # Open a string buffer to write the CSV output
        buffer = StringIO()

        # Write the header row
        fieldnames = ["name", "address", "phone_number"]
        writer = csv.DictWriter(buffer, fieldnames=fieldnames)
        writer.writeheader()

        # Write each PersonalData object to the CSV buffer
        for record in records:
            writer.writerow(record.__dict__)

        # Get the CSV output as a string
        csv_data = buffer.getvalue()

        # Close the buffer and return the CSV data
        buffer.close()

        return csv_data

    def deserialize(self, serialized_records: str) -> List[PersonalData]:
        """
        Deserialize records from a CSV format.

        Args:
            serialized_records (str): Serialized records in CSV format.

        Returns:
            List[PersonalData]: A list of deserialized PersonalData objects.

        Raises:
            ValueError: If no records are found to deserialize or if the input data is not valid CSV format.
        """
        # Call the base class implementation
        super().deserialize(serialized_records)

        # Open a string buffer to read the CSV data
        buffer = StringIO(serialized_records)

        # Read the CSV data and convert to a list of dictionaries
        reader = csv.DictReader(buffer)
        csv_data = list(reader)

        # Close the buffer
        buffer.close()

        # Convert the list of dictionaries to a list of PersonalData objects
        records = []
        for record_data in csv_data:
            try:
                name = record_data["name"]
                address = record_data["address"]
                phone_number = record_data["phone_number"]
                records.append(PersonalData(name, address, phone_number))
            except KeyError as e:
                raise ValueError(f"Missing required field: {e}")

        return records
