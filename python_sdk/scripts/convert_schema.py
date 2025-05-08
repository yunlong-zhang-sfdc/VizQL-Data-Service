import json


def get_component_by_ref(schema, ref_path):
    component_name = ref_path.split("/")[-1]
    return schema["components"]["schemas"][component_name]


def convert_schema(input_file, output_file):
    """
    Workaround for OpenAPI schema by restructuring Field and FilterField components to be
    able to generate the python client classes
    """
    with open(input_file, "r") as f:
        schema = json.load(f)

    field_type_map = {0: "SimpleField", 1: "AggregatedField", 2: "CalculatedField"}

    filter_field_type_map = {
        0: "SimpleFilterField",
        1: "AggregatedFilterField",
        2: "CalculatedFilterField",
    }

    field_oneof = schema["components"]["schemas"]["Field"]["oneOf"]
    new_components = {}

    for i, field_def in enumerate(field_oneof):
        allof = field_def["allOf"]
        field_base_ref = allof[0]["$ref"]
        field_base = get_component_by_ref(schema, field_base_ref)

        component_name = field_type_map[i]

        new_properties = field_def["properties"].copy()
        for prop_name, prop_value in field_def["properties"].items():
            if field_base["properties"].get(prop_name):
                new_properties[prop_name] = field_base["properties"][prop_name]

        field_def["properties"] = new_properties
        if "required" in field_def:
            field_def["required"] = list(
                set(field_def["required"] + field_base["required"])
            )

        new_components[component_name] = field_def
        del new_components[component_name]["allOf"]

    schema["components"]["schemas"]["Field"] = {
        "oneOf": [
            {"$ref": f"#/components/schemas/{field_type_map[i]}"}
            for i in range(len(field_oneof))
        ]
    }

    # Reverse oneOf array
    schema["components"]["schemas"]["Field"]["oneOf"].reverse()

    filter_field_oneof = schema["components"]["schemas"]["FilterField"]["oneOf"]

    for i, option in enumerate(filter_field_oneof):
        filter_def = option
        component_name = filter_field_type_map[i]
        new_components[component_name] = filter_def

    schema["components"]["schemas"]["FilterField"] = {
        "oneOf": [
            {"$ref": f"#/components/schemas/{filter_field_type_map[i]}"}
            for i in range(len(filter_field_oneof))
        ]
    }
    schema["components"]["schemas"]["FilterField"]["oneOf"].reverse()

    schema["components"]["schemas"].update(new_components)
    del schema["components"]["schemas"]["FieldBase"]

    with open(output_file, "w") as f:
        json.dump(schema, f, indent=4)


if __name__ == "__main__":
    convert_schema("../VizQLDataServiceOpenAPISchema.json", "build/temp_schema.json")
