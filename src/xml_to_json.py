import xmltodict
import json


def convert_xml_to_json(xml_file_path):
    try:
        # Open and read the XML file
        with open(xml_file_path, 'r') as xml_file:
            xml_content = xml_file.read()

        # Convert XML to dictionary using xmltodict
        xml_dict = xmltodict.parse(xml_content)

        # Convert dictionary to JSON
        json_data = json.dumps(xml_dict, indent=4)
        return json_data

    except Exception as e:
        print(f"Error while converting XML to JSON: {e}")
        return None
