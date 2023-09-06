import csv
from io import StringIO

from .base_display_fmt import BaseDisplayFormatter


class CSVDisplayFormatter(BaseDisplayFormatter):
    """
    A class to represent a CSV output formatter.
    """

    def display_format(self, records: list) -> str:
        """
        Format the records into a CSV output.

        Args:
            records (list): A list of records to be formatted.

        Returns:
            str: The formatted CSV output.
        """
        # Create a StringIO object to write the CSV data to
        output = StringIO()
        writer = csv.writer(output)

        # Write the header row in lowercase
        writer.writerow(["name", "address", "phone number"])

        # Loop through each record and write a row for each record
        for record in records:
            writer.writerow([record.name, record.address, record.phone_number])

        # Get the CSV data as a string and return it
        csv_data = output.getvalue()

        return csv_data
