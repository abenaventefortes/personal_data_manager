import argparse

from .api import PersonalDataAPI
from .models.personal_data import PersonalData


def main() -> None:
    """
    Entry point for the Personal Data Manager command-line application.
    """

    # Initialize the command-line argument parser
    parser = argparse.ArgumentParser(description="Personal Data Manager")

    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest="command", required=True, help="Subcommands")

    # Add record subcommand
    add_parser = subparsers.add_parser("add", help="Add a new record to the dataset")
    add_parser.add_argument("-n", "--name", required=True, help="Name of the person")
    add_parser.add_argument("-a", "--address", required=True, help="Address of the person")
    add_parser.add_argument("-p", "--phone_number", required=True, help="Phone number of the person")

    # Display subcommand
    display_parser = subparsers.add_parser("display", help="Display records in the dataset")
    display_parser.add_argument("-fmt", "--format", default="text",
                                help="Output format (default: text). Supported formats: text, csv, html, yaml")

    # Convert subcommand
    convert_parser = subparsers.add_parser("convert", help="Convert dataset to another format and save to a file")
    convert_parser.add_argument("-f", "--format", required=True,
                                help="Output format. Supported formats: csv, json, xml, yaml, text, html")
    convert_parser.add_argument("-o", "--output", help="File path to save the serialized data to")
    convert_parser.add_argument("-p", "--preview", action="store_true",
                                help="Display output without saving to a file if set, even if --output is also specified")

    # Filter subcommand
    filter_parser = subparsers.add_parser("filter",
                                          help="Filter records based on search criteria and display the results")
    filter_parser.add_argument("-f", "--field",
                               help="Field to filter records by (e.g., 'name', 'address', 'phone_number')")
    filter_parser.add_argument("-p", "--pattern",
                               help="Pattern to filter records by field (accepts SQL LIKE or glob syntax)")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Create an instance of the PersonalDataAPI class
    api = PersonalDataAPI()

    # Handle the "add" command
    if args.command == "add":
        # Create a new PersonalData object and add it to the dataset
        personal_data = PersonalData(args.name, args.address, args.phone_number)
        api.add_record(personal_data)
        print(f"Record added: {personal_data}")

    # Handle the "display" command
    elif args.command == "display":
        # Display records in the specified format
        print(f"Displaying records in {args.format} format:")
        api.display_records(output_format=args.format)

    # Handle the "convert" command
    elif args.command == "convert":
        # Convert the dataset to the specified format
        print(f"Converting dataset to {args.format} format:")
        if args.preview:
            print(f"Previewing data in {args.format} format:")
            api.convert_dataset(output_format=args.format)
        elif args.output:
            api.convert_dataset(output_format=args.format, file_path=args.output)
        else:
            parser.error("Either --preview or --output must be specified.")

    # Handle the "filter" command
    elif args.command == "filter":
        # Filter the records based on the search criteria and display the results
        if args.pattern:
            if "*" in args.pattern or "?" in args.pattern:
                records = api.filter_records(field=args.field, pattern=args.pattern, use_glob=True)
            else:
                records = api.filter_records(field=args.field, pattern=args.pattern)
        else:
            records = api.filter_records(field=args.field)

        if not records:
            print(f"No records found with field '{args.field}' matching pattern '{args.pattern}'")
        else:
            for record in records:
                print(f"{record.name}, {record.address}, {record.phone_number}")

    # Display the help message if an invalid command is entered
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
