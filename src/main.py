import os
from xml_to_json import convert_xml_to_json
from json_to_xml import convert_json_to_xml


def main():
    # Get the absolute path of the Resources directory
    base_path = os.path.dirname(os.path.abspath(__file__))
    resources_path = os.path.join(base_path, "Resources")

    # XML to JSON
    xml_file_path = os.path.join(resources_path, "data.xml")
    json_result = convert_xml_to_json(xml_file_path)
    print("XML to JSON:")
    print(json_result)

    # JSON to XML
    json_file_path = os.path.join(resources_path, "data.json")
    xml_result = convert_json_to_xml(json_file_path)
    print("\nJSON to XML:")
    print(xml_result)


if __name__ == "__main__":
    main()
