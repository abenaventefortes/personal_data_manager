# Getting Started

Welcome to the Personal Data Manager! 

This guide will walk you through the basics of using the Personal Data Manager API to manage personal data records and perform serialization and deserialization in multiple formats (JSON, XML, CSV, and YAML)

To start using the Personal Data Manager API, follow these steps:

### Import the API and the necessary components:


      from personal_data_manager.api import PersonalDataAPI
      from personal_data_manager.models import PersonalData
      from personal_data_manager.serializers.ser_factory import SerializerFactory
      from personal_data_manager.output_formatters.output_fmt_factory import DisplayFormatterFactory

### Create a PersonalDataAPI instance:

      api = PersonalDataAPI()

### Add, update, and delete records:

#### Add a record
    api.add_record(PersonalData("John Doe", "123 Main St", "555-908-1234"))

Since there is no direct method for updating or deleting records in the provided API, you can use the following workaround to achieve the desired functionality:

#### Update a record
    record = api.get_all_records()[0]
    api.cursor.execute("UPDATE personal_data SET name = ? WHERE name = ? AND address = ? AND phone_number = ?", ("Jane Doe", record.name, record.address, record.phone_number))
    api.conn.commit()

#### Delete a record
    record_to_delete = api.filter_records("name", "John Doe")[0]
    api.cursor.execute("DELETE FROM personal_data WHERE name = ? AND address = ? AND phone_number = ?", (record_to_delete.name, record_to_delete.address, record_to_delete.phone_number))
    api.conn.commit()

This method directly manipulates the SQLite database to update and delete records.

### Filter records based on the provided field and value:

      # Filter records by name
      filtered_records = api.filter_records("name", "*Doe*")

### Serialize and deserialize records:

      # Serialize records to JSON
      serializer_factory = SerializerFactory()
      json_serializer = serializer_factory.create_serializer("json")
      serialized_data = json_serializer.serialize(api.records)
      
      # Deserialize records from JSON
      deserialized_records = json_serializer.deserialize(serialized_data)

### Display records in the specified output format:

      # Create an HTML formatter instance and display records in HTML format
      output_formatter_factory = DisplayFormatterFactory()
      html_formatter = output_formatter_factory.create_formatter("html", api.records)
      api.display_records("html")