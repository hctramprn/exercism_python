import re


class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    # Perform regular expression substitutions to preprocess the input_string
    input_string = re.sub(r"(?<=\w);(?=\w)", "semicolon", input_string)
    input_string = re.sub(r"\\\\", "doubleescape", input_string)
    input_string = re.sub(r"\\\n", "", input_string)
    input_string = re.sub(r"\\", "", input_string)
    input_string = re.sub(r"\t", " ", input_string)
    input_string = re.sub(r"\n", "newline", input_string)

    # Find patterns for various error conditions and raise ValueErrors if found
    pattern_no_delimiter = re.findall(r"\(;\w\)", input_string)
    pattern_lowercase = re.findall(
        r"(?<=;)([a-z]+\[[\w\s\\n\(\)\[\]]*\])", input_string
    )
    pattern_mixcases = re.findall(
        r"(?<=;)([A-Z]+[a-z]+\[[\w\s\\n\(\)\[\]]*\])", input_string
    )

    if not input_string:
        raise ValueError("tree missing")
    elif input_string == "()":
        raise ValueError("tree with no nodes")
    elif input_string == ";":
        raise ValueError("tree missing")
    elif pattern_no_delimiter:
        raise ValueError("properties without delimiter")
    elif pattern_lowercase or pattern_mixcases:
        raise ValueError("property must be in uppercase")
    elif input_string == "(;)":
        return SgfTree()

    # Regular expression pattern to find properties and children in the input_string
    pattern = r"(?<=;)([A-Z]+\[[\w\s\\n\(\)\[\]=]*\])"
    matches = re.findall(pattern, input_string)
    properties, *children_lst = matches

    # Regular expression pattern to extract individual properties
    properties_pattern = r"([A-Z]+\[.*\])(?=\w+\[)|([A-Z]+\[.*\])"
    prop_all = re.findall(properties_pattern, properties)

    properties_lst = []
    for tup in prop_all:
        for val in tup:
            if val:
                properties_lst.append(val)

    properties_dict = dict()
    for prop in properties_lst:
        # Extract the key from the property
        key = re.match(r"[A-Z]+(?=\[)", prop)[0]

        # Extract the value(s) from the property using regular expressions
        value_pattern = r"(?<=[A-Z]\[).*?(?=\]\[)|(?<=\[)\w*(?=\])|(?<=\[).*(?=\])"
        val_temp = re.findall(value_pattern, prop)
        val_temp = [val for val in val_temp if val]

        # Process escape sequences (e.g., "newline," "semicolon," "doubleescape") in values
        val = []
        for v in val_temp:
            if "newline" or "semicolon" in v:
                val.append(
                    v.replace("newline", "\n")
                    .replace("semicolon", ";")
                    .replace("doubleescape", "\\")
                )
            else:
                val.append(v)
        properties_dict[key] = val

    parsed_children_lst = []
    for child in children_lst:
        # Recursively parse the child nodes using the 'parse' function
        parsed_children_lst.append(parse(f"(;{child})"))

    if not children_lst:
        # If there are no children, return an SgfTree with only the properties
        return SgfTree(properties_dict)
    else:
        # Return an SgfTree with both properties and parsed children
        return SgfTree(properties_dict, parsed_children_lst)