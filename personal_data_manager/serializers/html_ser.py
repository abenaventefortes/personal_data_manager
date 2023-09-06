from typing import List

from .base_ser import BaseSerializer
from personal_data_manager.models.personal_data import PersonalData


class HTMLSerializer(BaseSerializer):
    """
    A class to represent an HTML serializer.
    """

    def serialize(self, records: List[PersonalData]) -> str:
        """
        Serialize the records into an HTML format.

        Args:
            records (list): A list of records to be serialized.

        Returns:
            str: The serialized HTML output.
        """
        # Call the base class implementation
        super().serialize(records)

        output = "<html>\n<body>\n<table>\n"
        # Loop through each record and append the record information to the output string
        for record in records:
            output += f"<tr><td>{record.name}</td><td>{record.address}</td><td>{record.phone_number}</td></tr>\n"
        output += "</table>\n</body>\n</html>"

        return output

    def deserialize(self, serialized_records: str) -> list:
        """
        Deserialize HTML data into a list of PersonalData objects.

        Args:
            serialized_records (str): The serialized data to be deserialized.

        Returns:
            list: A list of PersonalData objects.
        """
        # Call the base class implementation
        super().deserialize(serialized_records)

        from bs4 import BeautifulSoup
        soup = BeautifulSoup(serialized_records, 'html.parser')
        records = []
        # Loop through each row of the HTML table
        for row in soup.find_all("tr"):
            # Extract the data from each cell
            cells = row.find_all("td")
            if len(cells) == 3:
                name, address, phone_number = [cell.text.strip() for cell in cells]
                # Create a PersonalData object from the data
                record = PersonalData(name, address, phone_number)
                records.append(record)

        return records

