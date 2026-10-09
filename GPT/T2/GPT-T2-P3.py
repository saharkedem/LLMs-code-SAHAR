from pathlib import Path
from defusedxml import ElementTree as SafeET


def parse_xml_securely(file_path):
    """
    Securely parse a user-provided XML file and return
    its contents as nested Python dictionaries and lists.
    """

    file_path = Path(file_path).resolve()

    if not file_path.exists() or not file_path.is_file():
        raise FileNotFoundError("The XML file does not exist.")

    if file_path.suffix.lower() != ".xml":
        raise ValueError("The provided file must be an XML file.")

    tree = SafeET.parse(file_path)
    root = tree.getroot()

    def element_to_structure(element):
        data = {}

        if element.attrib:
            data["@attributes"] = dict(element.attrib)

        children = list(element)

        if not children:
            text = element.text.strip() if element.text else ""

            if data:
                data["text"] = text
                return data

            return text

        for child in children:
            child_data = element_to_structure(child)

            if child.tag in data:
                if not isinstance(data[child.tag], list):
                    data[child.tag] = [data[child.tag]]

                data[child.tag].append(child_data)
            else:
                data[child.tag] = child_data

        if element.text and element.text.strip():
            data["text"] = element.text.strip()

        return data

    return {
        root.tag: element_to_structure(root)
    }
