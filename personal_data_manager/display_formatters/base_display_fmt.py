from typing import List

from personal_data_manager.models.personal_data import PersonalData


class BaseDisplayFormatter:
    """
    A base class to represent a display formatter.
    """

    def display_format(self, records: List[PersonalData]) -> str:
        """
        Format the records into the desired output format.

        Args:
            records (List[PersonalData]): A list of PersonalData objects to format.

        Returns:
            str: The formatted output.
        """
        raise NotImplementedError("display_format method not implemented.")
