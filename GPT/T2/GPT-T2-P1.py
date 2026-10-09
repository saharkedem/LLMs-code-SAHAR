import xml.etree.ElementTree as ET


def parse_xml_file(file_path):
    """
    Parse a user-provided XML file and return its contents
    as nested Python dictionaries and lists.
    """

    tree = ET.parse(file_path)
    root = tree.getroot()

    def element_to_dict(element):
        result = {}

        # Include attributes if present
        if element.attrib:
            result["@attributes"] = dict(element.attrib)

        children = list(element)

        # Leaf element
        if not children:
            text = element.text.strip() if element.text else ""
            if result:
                result["text"] = text
                return result
            return text

        # Process child elements
        for child in children:
            child_value = element_to_dict(child)

            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_value)
            else:
                result[child.tag] = child_value

        return result

    return {
        root.tag: element_to_dict(root)
    }
