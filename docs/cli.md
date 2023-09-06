# Personal Data Manager CLI

The Personal Data Manager package provides a command-line interface (CLI) for managing personal data records. 

This document describes the available commands and their usage.

The CLI includes the following commands:

* **_add:_** Add a new personal data record.
* _**display:**_ Display personal data records.
* _**convert:**_ Convert the dataset to another format.
* _**filter:**_ Filter personal data records based on search criteria.

### Add

To add a new personal data record, use the add command followed by the -n, -a, and -p options with their respective values:

    personal_data_manager add -n "Name" -a "Address" -p "Phone Number"

### Display

To display personal data records, use the display command:

    personal_data_manager display

You can also specify an output format using the --format option:

    personal_data_manager display --format json

### Convert

To convert the dataset to another format, use the convert command followed by the desired output format and the -o option with the output file path:

    personal_data_manager convert -f json -o output_file.json

To preview the output without saving it to a file, use the --preview flag:

    personal_data_manager convert -f json --preview

### Filter

To filter personal data records based on a specific field and pattern, use the filter command followed by the -f option for the field name and the -p option for the pattern:

    personal_data_manager filter -f name -p "John*"

Valid field options are: name, address, and phone_number.

For more details on using the Personal Data Manager, please refer to the API documentation and the [Getting Started](/docs/getting_started.md).