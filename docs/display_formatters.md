# Display Formatters

The Personal Data Manager API supports multiple output formats to display records in a user-friendly way. 

These formats currently include text, HTML, CSV and YAML.

Each format has a corresponding output formatter class:

    TextDisplayFormatter: Handles text output formatting.
    HTMLDisplayFormatter: Handles HTML output formatting.
    CSVDisplayFormatter: Handles CSV output formatting.
    YAMLDisplayFormatter: Handles YAML output formatting.

These output formatters are automatically used by the PersonalDataManager class when you call the **_display_records()_** method.

If you wish to add more output formats, please refer to [Adding Support For New Formats](/docs/extending_formats.md).