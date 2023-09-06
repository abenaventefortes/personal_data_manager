from .base_display_fmt import BaseDisplayFormatter


class HTMLDisplayFormatter(BaseDisplayFormatter):
    """
    A class to represent an HTML output formatter.
    """

    def display_format(self, records: list) -> str:
        """
        Format the records into an HTML output.

        Args:
            records (list): A list of records to be formatted.

        Returns:
            str: The formatted HTML output.
        """
        output = "<html>\n<head>\n<title>Personal Data</title>\n</head>\n<body>\n<table>\n"
        output += "<tr><th>Name</th><th>Address</th><th>Phone Number</th></tr>\n"

        # Loop through each record and append the record information to the output string
        for record in records:
            output += f"<tr><td>{record.name}</td><td>{record.address}</td><td>{record.phone_number}</td></tr>\n"

        output += "</table>\n</body>\n</html>"

        return output

