# SQLite Database

The Personal Data Manager API uses an SQLite database to store personal data records. 

The SQLite database file is named **_address_book.db_** and is located in the "data" directory within the "personal_data_manager" package.

When using the Personal Data Manager API, make sure that your current working directory is the **_personal_data_manager_** package, as the database is located in **_personal_data_manager/data/address_book.db_**. 

Alternatively, you can also make sure that your current working directory contains a **_data/address_book.db_** folder/file structure.

To access the SQLite database, the PersonalDataAPI class initializes a connection to the database when it is instantiated. 

The API then uses the database connection to execute various SQL queries, such as adding, updating, or deleting records, as well as filtering and retrieving records. The database connection is closed when the PersonalDataAPI object is destroyed.