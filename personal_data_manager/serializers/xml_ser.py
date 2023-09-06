import xml.etree.ElementTree as et
from xml.dom import minidom
from typing import List

from .base_ser import BaseSerializer
from personal_data_manager.models.personal_data import PersonalData


class XMLSerializer(BaseSerializer):
    """
    A serializer for converting PersonalData objects to and from XML format.
    """

    def serialize(self, records: List[PersonalData]) -> str:
        """
        Serialize a list of PersonalData objects to XML format.

        Args:
            records (List[PersonalData]): A list of PersonalData objects.

        Returns:
            str: Serialized records in XML format.

        Raises:
            ValueError: If no records are found to serialize.
        """
        # Call the base class implementation
        super().serialize(records)

        # Create the root element of the XML document.
        root = et.Element("records")

        # Iterate over each record in the list of records.
        for record in records:
            # Create a new element for this record.
            record_element = et.SubElement(root, "record")

            # Iterate over each key-value pair in the record's dictionary.
            for key, value in record.__dict__.items():
                # Create a new element for this field.
                if key == 'phone_number':
                    field_element = et.SubElement(record_element, "phone_number")
                else:
                    field_element = et.SubElement(record_element, key)

                # Set the text of the field element to the value of the corresponding attribute.
                field_element.text = str(value)

        # Serialize the XML tree to a string, with pretty formatting.
        return minidom.parseString(et.tostring(root)).toprettyxml(indent="  ")

    def deserialize(self, serialized_records: str) -> List[PersonalData]:
        """
        Deserialize records from an XML format.

        Args:
            serialized_records (str): Serialized records in XML format.

        Returns:
            List[PersonalData]: A list of deserialized PersonalData objects.

        Raises:
            ValueError: If no records are found to deserialize or if the input data is not valid XML format.
        """
        # Call the base class implementation
        super().deserialize(serialized_records)

        try:
            # Parse the serialized XML into an ElementTree object.
            root = et.fromstring(serialized_records)
        except et.ParseError as e:
            raise ValueError(f"Invalid XML data: {e}")

        # Create an empty list to hold the deserialized records.
        records = []

        # Iterate over each <record> element in the root element.
        for record_element in root.findall("record"):
            # Create variables to hold the data for this record.
            name = None
            address = None
            phone_number = None

            # Iterate over each child element of the <record> element.
            for field_element in record_element:
                # Set the appropriate variable to the text value of the field element.
                if field_element.tag == "name":
                    name = field_element.text
                elif field_element.tag == "address":
                    address = field_element.text
                elif field_element.tag == "phone_number":
                    phone_number = field_element.text

            # Create a new PersonalData object from the record data and append it to the list of records.
            record = PersonalData(name=name, address=address, phone_number=phone_number)
            records.append(record)

        # Return the list of deserialized records.
        return records
