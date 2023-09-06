import unittest

from personal_data_manager.api import PersonalDataAPI
from personal_data_manager.models.personal_data import PersonalData


class TestAPI(unittest.TestCase):
    """Test the PersonalDataAPI class."""

    api = None

    @classmethod
    def setUpClass(cls) -> None:
        """Set up the test fixture."""
        cls.api = PersonalDataAPI()

    def setUp(self) -> None:
        """Set up the test case."""
        self.api.cursor.execute("DELETE FROM personal_data")
        self.api.conn.commit()

    def tearDown(self) -> None:
        """Tear down the test case."""
        self.api.cursor.execute("DELETE FROM personal_data")
        self.api.conn.commit()

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down the test fixture."""
        cls.api.conn.close()

    def test_add_record(self) -> None:
        """
        Test that a new record can be added to the dataset.
        """
        # Create a new PersonalData object
        record = PersonalData("John", "123 Main St", "555-908-1234")

        # Add the new PersonalData object to the PersonalDataAPI instance
        self.api.add_record(record)

        # Verify that the number of records in the PersonalDataAPI instance is 1
        self.assertEqual(len(self.api.get_all_records()), 1)

    def test_create_invalid_data_value_error(self):
        """
        Test that adding a record with invalid data raises a ValueError.
        """
        # Verify that a ValueError is raised when attempting to create an invalid record
        with self.assertRaises(ValueError):
            PersonalData(name="John", address="123 Main St", phone_number="6045-805-9874")

    def test_add_record_missing_args_type_error(self):
        """
        Test that creating a PersonalData object with missing arguments raises a TypeError.
        """
        with self.assertRaises(TypeError):
            PersonalData(name="John")

    def test_filter_records(self):
        """
        Test that records can be filtered by a specified field and value.
        """
        # Create two new PersonalData objects
        record1 = PersonalData("John", "123 Main St", "555-908-1234")
        record2 = PersonalData("Jane", "456 Second St", "555-908-5678")

        # Add the new PersonalData objects to the PersonalDataAPI instance
        self.api.add_record(record1)
        self.api.add_record(record2)

        # Filter the records by name and verify that only one record is returned
        filtered_records = self.api.filter_records("name", "John")
        self.assertEqual(len(filtered_records), 1)

        # Verify that the filtered record is the correct one
        self.assertEqual(filtered_records[0].name, record1.name)
        self.assertEqual(filtered_records[0].address, record1.address)
        self.assertEqual(filtered_records[0].phone_number, record1.phone_number)

    def test_filter_invalid_field(self):
        """
        Test that filtering by an invalid field raises a ValueError.
        """
        # Verify that a ValueError is raised when attempting to filter by an invalid field
        with self.assertRaises(ValueError):
            self.api.filter_records("invalid_field", "value")

    def test_filter_value_not_found(self):
        """
        Test that filtering for a value that does not exist returns an empty list.
        """
        # Create a new PersonalData object
        record = PersonalData("John", "123 Main St", "555-908-1234")

        # Add the new PersonalData object to the PersonalDataAPI instance
        self.api.add_record(record)

        # Verify that filtering for a non-existent record returns an empty list
        self.assertEqual(self.api.filter_records("name", "Jane"), [])
