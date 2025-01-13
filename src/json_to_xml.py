import json
import xmltodict

def convert_json_to_xml(json_file_path):
    try:
        # Open and read the JSON file
        with open(json_file_path, 'r') as json_file:
            json_data = json.load(json_file)

        # Convert JSON to dictionary
        json_dict = json_data

        # Convert dictionary to XML using xmltodict
        xml_data = xmltodict.unparse(json_dict, pretty=True)
        return xml_data

    except Exception as e:
        print(f"Error while converting JSON to XML: {e}")
        return None
