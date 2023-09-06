import unittest
import textwrap

from personal_data_manager.models.personal_data import PersonalData
from personal_data_manager.display_formatters.csv_display_fmt import CSVDisplayFormatter
from personal_data_manager.display_formatters.html_display_fmt import HTMLDisplayFormatter
from personal_data_manager.display_formatters.display_fmt_factory import DisplayFormatterFactory
from personal_data_manager.display_formatters.text_display_fmt import TextDisplayFormatter


class TestOutputFormatters(unittest.TestCase):
    """
    A class for testing the output formatter classes.
    """

    def test_output_formatting(self) -> None:
        """
        Test the formatting of PersonalData objects using various output formats.
        """
        # Create a PersonalData object
        person = PersonalData("John Doe", "123 Main St", "555-908-1234")

        # Loop through the supported output formats and test output formatting
        for output_format in ["text", "html", "csv", "yaml"]:
            # Create an output formatter instance for the specified format
            formatter = DisplayFormatterFactory.create_formatter(output_format, [person])

            # Format the output and verify that it is a string
            formatted_output = formatter.display_format([person])
            self.assertIsInstance(formatted_output, str)

    def test_format_empty_list(self) -> None:
        """
        Test that formatting an empty list returns an empty string.
        """
        # Create an output formatter instance for the "text" format and an empty list
        formatter = DisplayFormatterFactory.create_formatter("text", [])

        # Format the output and verify that it is an empty string
        formatted_output = formatter.display_format([])
        self.assertEqual(formatted_output, "")

    def test_format_text_output(self):
        """
        Test that formatting a list of records in "text" format returns a string representation of the records in text format
        """
        # Create a list of PersonalData objects
        records = [
            PersonalData("John Doe", "123 Main St", "555-908-1234"),
            PersonalData("Jane Smith", "456 Second St", "555-908-5678")
        ]

        # Create a TextDisplayFormatter object and format the list of records
        formatter = TextDisplayFormatter()
        formatted_output = formatter.display_format(records)

        # Check that the formatted output matches the expected output
        expected_output = "John Doe\n123 Main St\n555-908-1234\n\nJane Smith\n456 Second St\n555-908-5678\n\n"
        self.assertEqual(formatted_output, expected_output)

    def test_format_csv_output(self):
        """
        Test that formatting a list of records in "csv" format returns a string representation of the records in CSV format
        """
        # Create a list of PersonalData objects
        records = [
            PersonalData("John Doe", "123 Main St", "555-908-1234"),
            PersonalData("Jane Smith", "456 Second St", "555-908-5678")
        ]

        # Create an CSVDisplayFormatter object and format the list of records
        formatter = CSVDisplayFormatter()
        formatted_output = formatter.display_format(records)

        # Check that the formatted output matches the expected output
        expected_output = "name,address,phone number\nJohn Doe,123 Main St,555-908-1234\nJane Smith,456 Second St," \
                          "555-908-5678\n"
        self.assertEqual(formatted_output.strip().replace('\r', ''), expected_output.strip())

    def test_format_html_output(self):
        """
        Test that formatting a list of records in "html" format returns a string representation of the records in HTML format
        """
        # Create a list of PersonalData objects
        records = [
            PersonalData("John Doe", "123 Main St", "555-908-1234"),
            PersonalData("Jane Smith", "456 Second St", "555-908-5678")
        ]

        # Create an HTMLDisplayFormatter object and format the list of records
        formatter = HTMLDisplayFormatter()
        formatted_output = formatter.display_format(records)

        # Check that the formatted output matches the expected output
        expected_output = textwrap.dedent('''\
                <html>
                <head>
                <title>Personal Data</title>
                </head>
                <body>
                <table>
                <tr><th>Name</th><th>Address</th><th>Phone Number</th></tr>
                <tr><td>John Doe</td><td>123 Main St</td><td>555-908-1234</td></tr>
                <tr><td>Jane Smith</td><td>456 Second St</td><td>555-908-5678</td></tr>
                </table>
                </body>
                </html>
            ''').rstrip()

        self.assertEqual(formatted_output, expected_output)

    def test_create_output_formatter_with_unsupported_format(self):
        """
        Test that creating an output formatter with an unsupported format raises a ValueError.
        """
        with self.assertRaises(ValueError):
            DisplayFormatterFactory.create_formatter("invalid_format", [])
