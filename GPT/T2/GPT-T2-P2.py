import xml.etree.ElementTree as ET


def parse_xml_to_structure(file_path):
    """
    Read an XML file, parse its contents, and return
    the extracted elements and values as a Python structure.
    """

    tree = ET.parse(file_path)
    root = tree.getroot()

    def parse_element(element):
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
            child_data = parse_element(child)

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
        root.tag: parse_element(root)
    }
