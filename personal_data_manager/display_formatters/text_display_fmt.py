from .base_display_fmt import BaseDisplayFormatter


class TextDisplayFormatter(BaseDisplayFormatter):
    """
    A class to represent a text output formatter.
    """

    def display_format(self, records: list) -> str:
        """
        Format the records into a text output.

        Args:
            records (list): A list of records to be formatted.

        Returns:
            str: The formatted text output.
        """
        output = ""

        # Loop through each record and append the record information to the output string
        for record in records:
            output += f"{record.name}\n{record.address}\n{record.phone_number}\n\n"

        return output
