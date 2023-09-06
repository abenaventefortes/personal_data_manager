import importlib
import os
import glob
from typing import Union, Any, List

# Base class for all serializers
from .base_ser import BaseSerializer

from .json_ser import JSONSerializer
from .yaml_ser import YAMLSerializer
from .xml_ser import XMLSerializer
from .csv_ser import CSVSerializer
from .text_ser import TextSerializer
from .html_ser import HTMLSerializer


class SerializerFactory:
    """
    A factory class to create and return the appropriate serializer based on the format string provided.
    """

    @staticmethod
    def create_serializer(output_format: str) -> Union[
        JSONSerializer, YAMLSerializer, XMLSerializer, CSVSerializer, TextSerializer, HTMLSerializer
    ]:
        """
        Create and return the appropriate serializer based on the format string provided.

        Args:
            output_format (str): The desired serialization format.

        Returns:
            Union[JSONSerializer, YAMLSerializer, XMLSerializer, CSVSerializer, TextSerializer, HTMLSerializer]: The appropriate serializer based on the format string provided.

        Raises:
            ValueError: If the provided format is not supported.
        """
        if output_format == "json":
            return JSONSerializer()
        elif output_format == "yaml":
            return YAMLSerializer()
        elif output_format == "xml":
            return XMLSerializer()
        elif output_format == "csv":
            return CSVSerializer()
        elif output_format == "text":
            return TextSerializer()
        elif output_format == "html":
            return HTMLSerializer()
        else:
            raise ValueError(f"Unsupported serialization format: {output_format}")

    @staticmethod
    def _get_format_from_file(serializer_file: str) -> Any | None:
        """
        Private helper method to get the format from a serializer file.

        Args:
            serializer_file (str): The file path of the serializer.

        Returns:
            Any | None: The format string from the serializer class name, or None if not found.
        """
        # Create the module name based on the serializer file name
        module_name = f"serializers.{os.path.splitext(serializer_file)[0]}"

        # Import the serializer module using the module name
        serializer_module = importlib.import_module(module_name)

        # Iterate through the module's objects
        for name, obj in serializer_module.__dict__.items():
            # Check if the object is a subclass of BaseSerializer and not BaseSerializer itself
            if isinstance(obj, type) and issubclass(obj, BaseSerializer) and obj is not BaseSerializer:
                # Extract the format string from the serializer class name and return it
                return name[:-9].lower()

        # If no format string is found, return None
        return None

    @staticmethod
    def get_supported_formats() -> List[str]:
        """
        Get a list of supported serialization formats.

        Returns:
            List[str]: A list of supported serialization formats.
        """
        # Get the path of the serializers folder
        serializers_folder = os.path.dirname(os.path.abspath(__file__))

        # Get a list of all the Python files in the serializers folder with a '_ser.py' suffix using glob
        serializer_files = glob.glob(os.path.join(serializers_folder, '*_ser.py'))

        # Initialize an empty list to store supported formats
        supported_formats = []

        # Iterate through all serializer files
        for f in serializer_files:
            # Get the format string from the serializer file using _get_format_from_file()
            fmt = SerializerFactory._get_format_from_file(os.path.basename(f))

            # If the format string is not None, add it to the supported_formats list
            if fmt:
                supported_formats.append(fmt)

        # Return the list of supported formats
        return supported_formats

    @staticmethod
    def get_serializer_instance(output_format: str) -> Union[
        JSONSerializer, YAMLSerializer, XMLSerializer, CSVSerializer, TextSerializer, HTMLSerializer, None
    ]:
        """
        Get the serializer instance for the given output format.

        Args:
            output_format (str): The desired serialization format.

        Returns:
            Union[JSONSerializer, YAMLSerializer, XMLSerializer, CSVSerializer, TextSerializer, HTMLSerializer, None]: The appropriate serializer based on the format string provided or None if the format is not supported.
        """
        try:
            serializer = SerializerFactory.create_serializer(output_format)
        except ValueError:
            serializer = None

        return serializer
