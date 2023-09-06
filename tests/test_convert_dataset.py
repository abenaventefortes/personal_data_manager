import os
import tempfile
import unittest

from personal_data_manager.api import PersonalDataAPI
from personal_data_manager.models.personal_data import PersonalData


class TestConvertDataset(unittest.TestCase):
    """Unit tests for the convert_dataset method of the PersonalDataAPI class."""

    def setUp(self) -> None:
        """Set up the test case."""
        self.api = PersonalDataAPI()

        # Create a new PersonalData object for testing
        self.record = PersonalData(name="Alice", address="123 Main St", phone_number="555-123-4567")

        # Add the new PersonalData object to the PersonalDataAPI instance
        self.api.add_record(self.record)

    def tearDown(self):
        """Clean up the test environment by removing the record and closing the database connection."""

        # Remove the record from the database
        self.api.cursor.execute("DELETE FROM personal_data WHERE name=?", ("Alice",))
        self.api.conn.commit()

        # Delete the PersonalDataAPI instance to close the database connection
        del self.api

    def test_convert_dataset_csv(self):
        """Test converting the dataset to CSV format."""
        # Create a temporary directory for the test and get the path to the file inside it
        with tempfile.TemporaryDirectory() as tempdir:
            file_path = os.path.join(tempdir, "address_book.csv")
            self.api.convert_dataset("csv", file_path)
            with open(file_path, "r") as f:
                # Skip the first line (header) before comparing
                f.readline()
                self.assertEqual(f.read(), '\nAlice,123 Main St,555-123-4567\n\n')

    def test_convert_dataset_html(self):
        """Test converting the dataset to HTML format."""
        # Create a temporary directory for the test and get the path to the file inside it
        with tempfile.TemporaryDirectory() as tempdir:
            file_path = os.path.join(tempdir, "address_book.html")
            self.api.convert_dataset("html", file_path)
            with open(file_path, "r") as f:
                # Skip the first two lines (HTML tags) before comparing
                f.readline()
                f.readline()
                self.assertEqual(f.read(), '<table>\n<tr><td>Alice</td><td>123 Main '
                                           'St</td><td>555-123-4567</td></tr>\n</table>\n</body>\n</html>')

    def test_convert_dataset_json(self):
        """Test converting the dataset to JSON format."""
        # Create a temporary directory for the test and get the path to the file inside it
        with tempfile.TemporaryDirectory() as tempdir:
            file_path = os.path.join(tempdir, "address_book.json")
            self.api.convert_dataset("json", file_path)
            with open(file_path, "r") as f:
                # Strip the newline character before comparing
                self.assertEqual(f.read().strip(),
                                 '[{"name": "Alice", "address": "123 Main St", "phone_number": "555-123-4567"}]')

    def test_convert_dataset_text(self):
        """Test converting the dataset to text format."""
        # Create a temporary directory for the test and get the path to the file inside it
        with tempfile.TemporaryDirectory() as tempdir:
            file_path = os.path.join(tempdir, "address_book.text")
            self.api.convert_dataset("text", file_path)
            with open(file_path, "r") as f:
                # Strip any whitespace before comparing
                self.assertEqual(f.read().strip(), 'Alice,123 Main St,555-123-4567')

    def test_convert_dataset_xml(self):
        """Test converting the dataset to XML format."""
        with tempfile.TemporaryDirectory() as tempdir:
            file_path = os.path.join(tempdir, "address_book.xml")
            self.api.convert_dataset("xml", file_path)
            with open(file_path, "r") as f:
                # Remove newlines and extra spaces from the file content to ensure accurate comparison
                file_content = f.read().replace("\n", "").replace(" ", "")
                expected_content = '<?xmlversion="1.0"?><records><record><name>Alice</name><address>123MainSt' \
                                   '</address><phone_number>555-123-4567</phone_number></record></records>'
                self.assertEqual(file_content, expected_content)

    def test_convert_dataset_yaml(self):
        """Test converting the dataset to YAML format."""
        # Create a temporary directory for the test and get the path to the file inside it
        with tempfile.TemporaryDirectory() as tempdir:
            file_path = os.path.join(tempdir, "address_book.yaml")
            # Convert the dataset to YAML format and save it to the file in the temporary directory
            self.api.convert_dataset("yaml", file_path)
            # Open the file and check that it contains the expected data
            with open(file_path, "r") as f:
                self.assertEqual(f.read(), '- address: 123 Main St\n  name: Alice\n  phone_number: 555-123-4567\n')

