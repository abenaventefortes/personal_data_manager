import unittest

from personal_data_manager.models.personal_data import PersonalData
from personal_data_manager.serializers.ser_factory import SerializerFactory


class TestSerializers(unittest.TestCase):
    """
    A class for testing the serializer classes.
    """

    def test_serialization(self):
        """
        Test the serialization and deserialization of PersonalData objects using various output formats.
        """
        person = PersonalData("John Doe", "123 Main St", "555-908-1234")

        for output_format in ["json", "yaml", "xml", "csv", "text", "html"]:
            # Create a serializer for the current format.
            serializer = SerializerFactory.create_serializer(output_format)

            # Serialize the PersonalData object.
            serialized = serializer.serialize([person])

            # Deserialize the serialized data.
            deserialized = serializer.deserialize(serialized)

            # Check that only one record was deserialized
            self.assertEqual(len(deserialized), 1)

            # Check that the deserialized record matches the original.
            self.assertEqual(str(deserialized[0]), str(person))

    def test_serialize_empty_list(self):
        """
        Test that serializing an empty list raises a ValueError.
        """
        for output_format in ["json", "yaml", "xml", "csv", "text", "html"]:
            # Create a serializer for the current format.
            serializer = SerializerFactory.create_serializer(output_format)

            # Serialize an empty list and check that a ValueError is raised.
            with self.assertRaises(ValueError):
                serializer.serialize([])

    def test_deserialize_empty_string(self):
        """
        Test that deserializing an empty string raises a ValueError.
        """
        for output_format in ["json", "yaml", "xml", "csv", "text", "html"]:
            # Create a serializer for the current format.
            serializer = SerializerFactory.create_serializer(output_format)

            # Deserialize an empty string and check that a ValueError is raised.
            with self.assertRaises(ValueError):
                serializer.deserialize("")

    def test_serialize_deserialize_list(self):
        """
        Test that serializing and deserializing a list of records returns an equivalent list of records.
        """
        records = [
            PersonalData("John Doe", "123 Main St", "555-908-1234"),
            PersonalData("Jane Smith", "456 Second St", "555-908-5678")
        ]
        for output_format in ["json", "yaml", "xml", "csv", "text", "html"]:
            # Create a serializer for the current format.
            serializer = SerializerFactory.create_serializer(output_format)

            # Serialize the list of records.
            serialized = serializer.serialize(records)

            # Deserialize the serialized data.
            deserialized = serializer.deserialize(serialized)

            # Check that the deserialized data is equivalent to the original list of records.
            for i in range(len(records)):
                self.assertEqual(str(deserialized[i]), str(records[i]))


if __name__ == "__main__":
    # Run the test suite.
    unittest.main()
