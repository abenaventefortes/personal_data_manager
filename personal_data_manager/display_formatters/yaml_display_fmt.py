from typing import List
import yaml

from personal_data_manager.models.personal_data import PersonalData
from .base_display_fmt import BaseDisplayFormatter


class YAMLDisplayFormatter(BaseDisplayFormatter):
    """
    A class for formatting PersonalData objects in YAML format.
    """

    def display_format(self, records: List[PersonalData]) -> str:
        """
        Format a list of PersonalData objects in YAML format.

        Args:
            records (List[PersonalData]): A list of PersonalData objects to format.

        Returns:
            str: A string representation of the PersonalData objects in YAML format.
        """
        # Convert the records to a dictionary
        data = {"personal_data": [record.to_dict() for record in records]}

        # Serialize the dictionary to YAML format
        return yaml.dump(data, sort_keys=False)
