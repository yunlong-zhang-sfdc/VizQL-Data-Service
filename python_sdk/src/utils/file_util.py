import json
import os

"""
Utility class to read files as json
"""


def read_json(dir, filename):
    filepath = os.path.join(dir, filename)

    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        return json.dumps(data)
    except:
        print(f"Error: File not found - {filepath}")
        return None


def read_and_return_json(filename):
    with open(filename) as f:
        data = json.load(f)
        return data
