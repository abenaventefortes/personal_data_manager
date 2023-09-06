# Serializers

The Personal Data Manager API currently supports four serialization formats: JSON, XML, CSV, TEXT, HTML and YAML. 

Each format has a corresponding serializer class for handling serialization and deserialization:

* **JSONSerializer** 
* **XMLSerializer** 
* **CSVSerializer** 
* **HTMLSerializer** 
* **TextSerializer** 
* **YAMLSerializer** 

These serializers are automatically used by the _**PersonalDataManager**_ class when you call the _**serialize_records**_ and **_deserialize_records_** methods.

## Getting Supported Formats

The SerializerFactory class provides a method get_supported_formats() that returns a list of supported serialization formats. This method dynamically discovers the serializers available under the serializers folder, making it easy to add or remove support for serialization formats without modifying the factory's code.

Example usage:
    
    from personal_data_manager.ser_factory import SerializerFactory
    
    supported_formats = SerializerFactory.get_supported_formats()
    print(supported_formats)

Output:

    ['json', 'xml', 'csv', 'html', 'text','yaml']

By following this approach, developers can easily extend the system to add support for additional storage formats or query a list of currently supported formats without modifying the core API code.

If you wish to add more serializing formats please look at extending_formats.md