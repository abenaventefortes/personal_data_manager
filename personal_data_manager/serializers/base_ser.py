from typing import List, NoReturn

from personal_data_manager.models.personal_data import PersonalData


class BaseSerializer:
    """
    The base class for all serializers. It defines the interface for serialization and deserialization.
    """

    def serialize(self, records: List[PersonalData]) -> NoReturn:
        """
        Serialize a list of records.

        Args:
            records (List[PersonalData]): A list of PersonalData objects.

        Returns:
            str: Serialized records.

        Raises:
            ValueError: If no records are found to serialize.
        """
        if not records:
            # Raise an error if no records are found to serialize
            raise ValueError("No records found to serialize")

    def deserialize(self, serialized_records: str) -> NoReturn:
        """
        Deserialize records from a serialized format.

        Args:
            serialized_records (str): Serialized records.

        Returns:
            List[PersonalData]: A list of deserialized PersonalData objects.

        Raises:
            ValueError: If no records are found to deserialize.
        """
        if not serialized_records:
            # Raise an error if no records are found to deserialize
            raise ValueError("No records found to deserialize")
