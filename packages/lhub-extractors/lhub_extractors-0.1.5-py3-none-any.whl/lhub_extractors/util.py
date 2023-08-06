from typing import List, Tuple
from pathlib import Path

import json 
import importlib

def import_workdir() -> Tuple[List[Exception], List[str]]:
    errors = []
    docstrings = []
    for file in Path(".").iterdir():
        if file.suffix == ".py":
            file_name = file.name[: -len(".py")]
            if "." in file_name:
                errors.append(f"Python files cannot contain dots: {as_module}")
                continue
            try:
                module = importlib.import_module(file_name)
                docstrings.append(module.__doc__)
            except Exception as ex:
                errors.append(ex)
    return errors, docstrings

def print_result(msg):
    print(f"[result] {msg}")

def invalid_extractor(code, error):
    raise InvalidExtractor(code, error)

def deser_output(output: str):
    prefix = "[result]"
    processed = ""
    for line in output.splitlines():
        if line.startswith(prefix):
            processed += line[len(prefix) :]
    try:
        return json.loads(processed)
    except json.decoder.JSONDecodeError:
        raise Exception(f"Could not parse JSON: {output}")

class InvalidExtractor(Exception):
    def __init__(self, key, message):
        super().__init__(f"{message} [{key}]")
