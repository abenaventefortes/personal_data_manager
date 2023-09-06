import os
import sqlite3
import re
from typing import List

from .serializers import SerializerFactory
from .models.personal_data import PersonalData
from .display_formatters.display_fmt_factory import DisplayFormatterFactory


class PersonalDataAPI:
    """The API class for managing personal data records."""

    def __init__(self) -> None:
        self.serializer_factory = None
        self.connection = None

        # instantiate the SerializerFactory class
        self.serializer_factory = SerializerFactory()

        # Initialize a connection to the SQLite database
        self.conn = sqlite3.connect("data/address_book.db")
        self.cursor = self.conn.cursor()

        # Check if the "personal_data" table already exists
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='personal_data'")
        result = self.cursor.fetchone()

        if result is None:
            # Create the "personal_data" table if it does not already exist
            self.cursor.execute(
                """
                CREATE TABLE personal_data (
                    name TEXT,
                    address TEXT,
                    phone_number TEXT
                )
                """
            )

    def __del__(self) -> None:
        try:
            # Close the database connection when the object is destroyed
            self.conn.close()
        except AttributeError:
            print(
                "Error: Database not found."
                "Please check that the current working directory is the 'personal_data_manager' package, "
                "as the database is located in 'personal_data_manager/data/address_book.db'."
                "Or make sure that your current working directory contains a data/address_book.db folder/file structure"
            )

    def add_record(self, record: PersonalData) -> None:
        """
        Add a new record to the dataset.

        Args:
            record (PersonalData): The record to add to the dataset.

        Raises:
            ValueError: If the record is not an instance of PersonalData.
            Exception: If there is an error executing the SQL query.
        """
        if not isinstance(record, PersonalData):
            raise ValueError("Record must be an instance of PersonalData.")

        # Insert the record into the "personal_data" table
        try:
            self.cursor.execute(
                "INSERT INTO personal_data (name, address, phone_number) VALUES (?, ?, ?)",
                (record.name, record.address, record.phone_number),
            )
            self.conn.commit()
        except Exception as e:
            print(f"Error adding record: {str(e)}")

    def get_all_records(self) -> List[PersonalData]:
        """
        Get all records from the dataset.

        Returns:
            List[PersonalData]: A list of all records in the dataset.
        """
        # Retrieve all records from the "personal_data" table
        query = "SELECT * FROM personal_data"
        self.cursor.execute(query)
        records = []
        for row in self.cursor.fetchall():
            record = PersonalData(*row)
            records.append(record)

        return records

    def display_records(self, output_format: str = "text", records=None) -> None:
        """
        Display records in the specified output format.

        Args:
            records: An optional list of records to display. If not provided, all records in the database will be displayed.
            output_format (str): The output format (default: "text").

        Raises:
            ValueError: If the output format is not supported.

        Raises:
            ValueError: If no records are found in the database.
        """
        # Retrieve all records from the "personal_data" table if records is not provided
        if records is None:
            records = self.get_all_records()
            if not records:
                raise ValueError("No records found in the database.")

        # Create a formatter instance based on the specified output format
        try:
            formatter = DisplayFormatterFactory.create_formatter(output_format, records)
        except ValueError:
            print(f"Error: {output_format} is not a supported output format.")
            return

        # Use the formatter to format the records and print the output
        formatted_output = formatter.display_format(records)
        print(formatted_output)

    def convert_dataset(self, output_format: str, file_path: str, preview: bool = False) -> None:
        """
        Convert the dataset to the specified format and optionally save to a file.

        Args:
            output_format (str): The output format.
            file_path (str): The file to save the serialized data to (optional).
            preview (bool): Whether to preview the output without saving to a file (optional).

        Raises:
            ValueError: If the output format is not supported.
        """
        # Retrieve records from the "personal_data" table
        self.cursor.execute("SELECT * FROM personal_data")
        rows = self.cursor.fetchall()

        # Create a list of PersonalData objects from the retrieved rows
        records = []
        for row in rows:
            personal_data = PersonalData(*row)
            records.append(personal_data)

        # Create a serializer instance based on the specified output format
        serializer = self.serializer_factory.get_serializer_instance(output_format)
        if serializer is None:
            print(f"Error: {output_format} is not a supported serialization format.")
            return

        # Use the serializer to serialize the records and print or save the output
        serialized_data = serializer.serialize(records)
        if preview:
            print(serialized_data)
        else:
            abs_file_path = os.path.abspath(file_path)
            directory_path = os.path.dirname(abs_file_path)
            if not os.path.isdir(directory_path):
                print(f"Error: the directory '{directory_path}' does not exist.")
                return

            # Attempt to save the file to the specified directory
            try:
                # Use the default file name, "address_book.{output_format}"
                # unless a file with that name already exists
                file_name = f"{directory_path}/address_book.{output_format}"
                index = 1

                # If the file already exists, add a digit to differentiate it
                while os.path.exists(file_name):
                    file_name = f"{directory_path}/address_book_{index}.{output_format}"
                    index += 1

                # Write the serialized data to the file
                with open(file_name, "w") as f:
                    f.write(serialized_data)
                print(f"Serialized data saved to {os.path.abspath(file_name)}.")

            # Handle exceptions that may occur when saving the file
            except PermissionError as e:
                print(f"Error saving serialized data to {abs_file_path}: {e}")
                print("Make sure you have administrator privileges or the folder has write permissions.")
            except OSError as e:
                print(f"Error saving serialized data to {abs_file_path}: {e}")

    def filter_records(self, field: str, pattern: str = "", use_glob: bool = False) -> List[PersonalData]:
        """
        Filter records based on the provided field and pattern.

        Args:
            field (str): The field to filter records by (e.g., 'name', 'address', 'phone_number').
            pattern (str): The pattern to match in the specified field using SQL LIKE or glob pattern matching (default "").
            use_glob (bool): If True, use glob pattern matching. If False (default), use SQL LIKE.

        Returns:
            List[PersonalData]: A list of filtered records that match the provided field and pattern.

        Raises:
            ValueError: If the field is not valid.
            Exception: If there is an error executing the SQL query.
        """
        # Define a list of valid fields and raise an error if an invalid field is provided
        valid_fields = ["name", "address", "phone_number"]
        if field not in valid_fields:
            raise ValueError(f"Invalid field '{field}'. Valid fields are: {valid_fields}")

        # Define the SQL query based on the provided field and pattern
        if pattern and use_glob:
            query = f"SELECT name, address, phone_number FROM personal_data WHERE {field} GLOB ?"
        elif pattern:
            query = f"SELECT name, address, phone_number FROM personal_data WHERE {field} LIKE ?"
        else:
            query = f"SELECT name, address, phone_number FROM personal_data WHERE {field} IS NOT NULL"

        # Execute the query and fetch the results
        try:
            self.cursor.execute(query, (pattern,))
            rows = self.cursor.fetchall()
        except Exception as e:
            print(f"Error executing query: {str(e)}")
            return []

        # Standardize the formatting of the returned records
        personal_data_list = []
        for row in rows:
            # Use tuple unpacking to assign variables to the row elements
            name, address, phone_number = row

            # Clean up the formatting of the phone number
            phone_number = re.sub(r'(\d{3})(\d{3})(\d{4})', r'\1-\2-\3', phone_number)

            # Create a new PersonalData object with the standardized formatting
            personal_data = PersonalData(name.strip().title(), address.strip().title(), phone_number.strip())
            personal_data_list.append(personal_data)

        return personal_data_list
