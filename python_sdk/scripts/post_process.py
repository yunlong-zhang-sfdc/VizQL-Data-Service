import os
import re


def convert_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Global class name replacements
    replacements = {
        "Field2": "AggregatedField",
        "Field3": "CalculatedField",
        "Field1": "SimpleField",
        "FieldModel": "TabField",
        "Optional[List[Filter]]": "Optional[List[TabFilter]]",
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    # Add extra='forbid' to all Filter subclasses
    filter_classes = [
        "MatchFilter",
        "QuantitativeNumericalFilter",
        "QuantitativeDateFilter",
        "SetFilter",
        "RelativeDateFilter",
        "TopNFilter",
    ]

    # Add exclude_none and exclude_unset to all model_config
    pattern = r"class ([^(]+)\(([^)]*)\):\n    model_config = ConfigDict\(\n        ([^)]*)\n    \)"

    def add_config_options(match):
        class_name = match.group(1).strip()
        base_class = match.group(2).strip()
        config = match.group(3)
        # Add extra='forbid' for filter classes
        if class_name in filter_classes:
            if "extra" not in config:
                config += "\n        extra='forbid',"
        if "exclude_none" not in config:
            config += "\n        exclude_none=True,"
        if "exclude_unset" not in config:
            config += "\n        exclude_unset=True,"
        return f"class {class_name}({base_class}):\n    model_config = ConfigDict(\n        {config}\n    )"

    content = re.sub(pattern, add_config_options, content)

    # Add TabFilter class at the end of file
    tab_filter_code = """
class TabFilter(RootModel[Union[
    MatchFilter, QuantitativeNumericalFilter, QuantitativeDateFilter, SetFilter, RelativeDateFilter, TopNFilter]]):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    root: Union[
        MatchFilter, QuantitativeNumericalFilter, QuantitativeDateFilter, SetFilter, RelativeDateFilter, TopNFilter]
"""
    content += tab_filter_code

    # Write to output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    convert_file("src/api/openapi_api-raw.py", "src/api/openapi_api.py")
    os.remove("src/api/openapi_api-raw.py")
