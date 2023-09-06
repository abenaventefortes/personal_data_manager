# Adding Support for New Formats
This document provides a guide on how to add support for new formats in the Personal Data Manager API.

It outlines the steps to follow when adding support for new serialization, output formats and update the unit tests.

When adding support for a new format, you should only include a display format if it's human-readable. Examples of human-readable formats are text, HTML, and CSV. 
### Add a new serialization format

To add support for a new serialization format, follow these steps:

* Create a new serializer class in the serializers folder. The class should inherit from the BaseSerializer class and implement the serialize() and deserialize() methods. Name the class with the format's name followed by Serializer and use the _ser.py file extension. For example, if you want to add support for the TOML format, create a file named toml_ser.py with a class named TOMLSerializer.

**_Example_**:

    # serializers/toml_ser.py
    from serializers.base_ser import BaseSerializer
    
    class TOMLSerializer(BaseSerializer):
        def serialize(self, records: List[PersonalData]) -> str:
            # Implement the serialization logic for TOML format

        def deserialize(self, serialized_data: str) -> List[PersonalData]:
            # Implement the deserialization logic for TOML format

* Ensure that the new serializer class is discoverable by the SerializerFactory class. The factory automatically detects serializer classes in the serializers folder that have filenames ending with _ser.py. If you followed the naming convention in step 1, the factory should automatically discover and use your new serializer class.
* Update the dependencies of the project, if necessary. If the new format requires external libraries, add those libraries to the project's dependencies.
* Test the new serializer class with the PersonalDataManager class. Once you have implemented the new serializer, you can use it with the PersonalDataManager class by specifying the new format when calling the serialize_records() and deserialize_records() methods.

**_Example_**:

    # Assuming the TOMLSerializer class has been implemented
    
    from personal_data_manager.api import PersonalDataManager
    
    manager = PersonalDataManager()
    
    # Use the new serializer by specifying the 'toml' format
    serialized_data = manager.serialize_records("toml")

By following these steps, you can easily extend the Personal Data Manager API to support additional serialization formats.

### Add a new display formatter
Create a new output formatter class in the output_formatters folder. The class should inherit from the BaseDisplayFormatter class and implement the display_format() method. Name the class with the format's name followed by Formatter and use the _fmt.py file extension. 

For example, if you want to add support for PDF format you can create a file named pdf_fmt.py in the output_formatters folder with a class named PDFFormatter that implements the display_format() method to generate PDF output.

By following these steps, you can easily extend the Personal Data Manager API to support additional serialization formats.

**_Example:_**

    # display_formatters/pdf_fmt.py
    from display_formatters.base_output_fmt import BaseDisplayFormatter
    
    class PDFDisplayFormatter(BaseDisplayFormatter):
        def display_format(self):
            # Implement the formatting logic for PDF format
            pass

After implementing the PDFDisplayFormatter class, you can use it with the PersonalDataAPI class by specifying the pdf format when calling the display_records() method:

    from personal_data_manager.api import PersonalDataAPI
    from personal_data_manager.output_formatters.output_fmt_factory import DisplayFormatterFactory
    
    api = PersonalDataAPI()
    api.add_record(PersonalData("John Doe", "123 Main St", "555-908-1234"))
    api.add_record(PersonalData("Jane Smith", "456 Second St", "555-908-5678"))
    
    output_formatter_factory = DisplayFormatterFactory()
    pdf_formatter = output_formatter_factory.create_formatter("pdf", api.records)
    pdf_output = pdf_formatter.display_format()
    
    api.display_records("pdf")  # display records in PDF format

Note that you may need to install additional dependencies to generate PDF output.
If so be sure to add them to the README.md

By following these steps, you can easily extend the Personal Data Manager API to support additional output formats.

### Updating Formats in Tests

If you have added a new serializer or output formatter, you may need to update the tests to include the new format. To do this, follow these steps:

#### Updating the Serializer Tests

To update the serializer tests with the new format, you'll need to add the new format to the **output_formats** list in the **test_serialization** method in the **_test_ser.py_** file:

    output_formats = ["json", "yaml", "xml", "csv", "toml", "new_format"]

#### Updating the Output Formatter Tests

To update the output formatter tests with the new format, add the new format to the list of supported output formats in the test_output_formatting method in the **_test_ouput_fmt.py_** file:

    for output_format in ["text", "html", "csv", "yaml", "new_format"]:

#### Adding New Test Methods

If you need to add new test methods for the new format, you can follow the existing test methods as a template. For example, you can create a new test method for the new format in the test_ouput_fmt.py file:


    def test_format_new_output(self):
        """
        Test that formatting a list of records in "new_format" returns a string representation of the records in the new format.
        """
        # Create a list of PersonalData objects
        records = [
            PersonalData("John Doe", "123 Main St", "555-908-1234"),
            PersonalData("Jane Smith", "456 Second St", "555-908-5678")
        ]
    
        # Create a NewFormatDisplayFormatter object and format the list of records
        formatter = NewFormatDisplayFormatter()
        formatted_output = formatter.display_format(records)
    
        # Check that the formatted output matches the expected output
        expected_output = "..."
        self.assertEqual(formatted_output, expected_output)

Make sure to replace the NewFormatDisplayFormatter with the actual display formatter class for the new format.

#### Updating the Dataset Conversion Tests

Finally, update the dataset conversion tests in the test_convert_dataset.py file by adding a new test method for the new format:

    def test_convert_dataset_new_format(self):
        """Test converting the dataset to the new format."""
        with tempfile.TemporaryDirectory() as tempdir:
            file_path = os.path.join(tempdir, "address_book.new_format")
            self.api.convert_dataset("new_format", file_path)
            with open(file_path, "r") as f:
                self.assertEqual(f.read().strip(), "...")

Replace "new_format" with the appropriate format name, and update the expected output string in the self.assertEqual() method.

By following these steps, you can update the tests to include the new format and ensure that your changes don't break the existing tests.