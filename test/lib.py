import json
import os


def load_json(file_path):
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_path)
    with open(file, mode='r') as fp:
        return json.load(fp)
