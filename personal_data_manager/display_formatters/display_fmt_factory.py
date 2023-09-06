from typing import List

from personal_data_manager.models.personal_data import PersonalData

from .base_display_fmt import BaseDisplayFormatter
from .text_display_fmt import TextDisplayFormatter
from .html_display_fmt import HTMLDisplayFormatter
from .csv_display_fmt import CSVDisplayFormatter
from .yaml_display_fmt import YAMLDisplayFormatter


class DisplayFormatterFactory:
    """
    A factory class to create and return the appropriate output formatter based on the format string provided.
    """

    @staticmethod
    def create_formatter(output_format: str, records: List[PersonalData]) -> BaseDisplayFormatter:
        """
        Create and return the appropriate output formatter based on the output_format string provided.

        Args:
            output_format (str): The desired output format.
            records (List[PersonalData]): A list of PersonalData objects to format.

        Returns:
            BaseDisplayFormatter: The appropriate output formatter based on the output_format string provided.

        Raises:
            ValueError: If the output_format is unsupported.
        """
        # Check the output_format and return the appropriate output formatter
        if output_format == "text":
            return TextDisplayFormatter()
        elif output_format == "html":
            return HTMLDisplayFormatter()
        elif output_format == "csv":
            return CSVDisplayFormatter()
        elif output_format == "yaml":
            return YAMLDisplayFormatter()
        else:
            raise ValueError(f"Unsupported output format: {output_format}")
