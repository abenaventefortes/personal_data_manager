import unittest

from personal_data_manager.models.personal_data import PersonalData


class TestPersonalData(unittest.TestCase):
    """
    A class for testing the PersonalData class.
    """

    def test_create_person(self) -> None:
        """
        Test that creating a PersonalData object with valid data returns an object with the correct attributes.
        """
        # Create a new PersonalData object
        person = PersonalData("John Doe", "123 Main St", "555-908-1234")

        # Verify that the object was created with the correct attributes
        self.assertEqual(person.name, "John Doe")
        self.assertEqual(person.address, "123 Main St")
        self.assertEqual(person.phone_number, "555-908-1234")

    def test_create_person_invalid_data(self):
        """
        Test that creating a PersonalData object with invalid data raises the appropriate error.
        """
        # Verify that creating a PersonalData object with an empty name raises a ValueError
        with self.assertRaises(ValueError):
            PersonalData("", "123 Animal St", "555-908-1234")

        # Verify that creating a PersonalData object with an empty address raises a ValueError
        with self.assertRaises(ValueError):
            PersonalData("John Doe", "", "555-908-1234")

        # Verify that creating a PersonalData object with an invalid phone number raises a ValueError
        with self.assertRaises(ValueError):
            PersonalData("John Doe", "123 Main St", "555-12-34")

        # Verify that creating a PersonalData object with a non-string name raises a TypeError
        with self.assertRaises(TypeError):
            PersonalData(123, "123 Main St", "555-908-1234")

        # Verify that creating a PersonalData object with a non-string address raises a TypeError
        with self.assertRaises(TypeError):
            PersonalData("John Doe", 123, "555-908-1234")

        # Verify that creating a PersonalData object with a non-string phone number raises a TypeError
        with self.assertRaises(TypeError):
            PersonalData("John Doe", "123 Main St", 5551234)


if __name__ == "__main__":
    unittest.main()
