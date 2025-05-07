#!/usr/bin/env python3
"""Script to automatically add docstrings to enum classes in the openapi_client folder."""

import os
from pathlib import Path
from typing import List, Tuple


def find_enum_classes(file_path: str) -> List[Tuple[str, List[str], int]]:
    """Find all enum classes and their values in a Python file."""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    enum_classes = []
    current_class = None
    values = []
    class_line = 0

    for i, line in enumerate(lines):
        line = line.strip()
        if line.startswith("class ") and "Enum" in line:
            if current_class:
                enum_classes.append((current_class, values, class_line))
            current_class = line.split("class ")[1].split("(")[0].strip()
            values = []
            class_line = i
        elif current_class and line and not line.startswith(("def ", '"""')):
            if "=" in line:
                value = line.split("=")[0].strip()
                values.append(value)

    if current_class:
        enum_classes.append((current_class, values, class_line))

    return enum_classes


def generate_enum_docstring(class_name: str, values: List[str]) -> str:
    """Generate a docstring for an enum class."""
    readable_name = " ".join(class_name.split("_")).title()

    docstring = f'"""{readable_name} enumeration.\n\n'
    docstring += f"This enum represents the {readable_name.lower()} values supported by the VizQL Data Service.\n\n"
    docstring += "Values:\n"

    for value in values:
        readable_value = " ".join(value.split("_")).title()
        docstring += f"    - {value}: {readable_value}\n"

    docstring += "\nExample:\n"
    docstring += f"    >>> {class_name}.{values[0]}\n"
    docstring += f"    {class_name}.{values[0]}\n"
    docstring += '"""'

    return docstring


def add_docstring_to_file(file_path: str) -> None:
    """Add docstrings to enum classes in a file."""
    enum_classes = find_enum_classes(file_path)
    if not enum_classes:
        return

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    modified = False
    # Process from bottom to top to avoid line number issues
    for class_name, values, line_no in sorted(
        enum_classes, key=lambda x: x[2], reverse=True
    ):
        # Get the indentation of the class definition
        indent = len(lines[line_no]) - len(lines[line_no].lstrip())

        # Generate and format the docstring
        docstring = generate_enum_docstring(class_name, values)
        docstring_lines = docstring.split("\n")
        formatted_docstring = "\n".join(
            " " * (indent + 4) + line for line in docstring_lines
        )

        # Find the next non-empty line after class definition
        next_line = line_no + 1
        while next_line < len(lines) and not lines[next_line].strip():
            next_line += 1

        # Insert the docstring after the class definition
        lines.insert(next_line, formatted_docstring + "\n")
        modified = True

    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"Added docstrings to {file_path}")


def main():
    """Main function to process all Python files in the openapi_client folder."""
    openapi_client_dir = Path(__file__).parent.parent / "openapi_client"

    for root, _, files in os.walk(openapi_client_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                add_docstring_to_file(file_path)


if __name__ == "__main__":
    main()
