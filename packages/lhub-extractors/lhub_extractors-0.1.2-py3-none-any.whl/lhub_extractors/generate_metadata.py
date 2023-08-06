from dataclasses_json import dataclass_json
from dataclasses import dataclass
from docstring_parser import parse
from typing import List

import inspect
import json

from lhub_integ.util import print_result, import_workdir, InvalidExtractor
from lhub_integ import feature_extractor

@dataclass
@dataclass_json
class FeatureExtractorColumn:
    name: str
    data_type: str
    description: str
    errors: List[str]

@dataclass
@dataclass_json
class FeatureExtractorMetadata:
    feature_extractor_name: str
    feature_extractor_description: str
    feature_extractor_columns: List[FeatureExtractorColumn]
    errors: List[str]

def generate_metadata():
    toplevel_errors = []
    errors, docstrings = import_workdir()
    for error in errors:
        if isinstance(error, SyntaxError):
            toplevel_errors.append(f"Failed to import module: {error}")
        elif isinstance(error, ImportError):
            toplevel_errors.append(
                f"Failed to import module (did you run bundle-extractors?): {error}"
            )
        elif isinstance(error, InvalidExtractor):
            toplevel_errors.append(
                f"Extractor was invalid: {error}"
            )
        else:
            toplevel_errors.append(
                f"Failed to import module (Unexpected error): {error}"
            )

    extractors = []
    for extractor in feature_extractor.all().values():
        extractor_function = extractor.function

        # Parse the docstring
        docs = extractor_function.__doc__
        parsed = parse(docs)

        errors = []
        if parsed.short_description or parsed.long_description:
            function_description = parsed.short_description or parsed.long_description
        else:
            function_description = None

        args, varargs, kwargs = inspect.getargs(extractor_function.__code__)
        if varargs:
            errors.append("Varargs are not supported")
        if kwargs:
            errors.append("Kwargs are not supported")

        feature_extractor_columns = []
        for param in parsed.params:
            param_errors = []
            arg_map = {}
            if param.arg_name is not None:
                arg_map['name'] = param.arg_name
            else:
                param_errors.append("Parameter name not provided")
            if param.description is not None:
                arg_map['description'] = param.description
            else:
                param_errors.append("Parameter description not provided")
            if param.type_name is not None:
                arg_map['type'] = param.type_name
            else:
                param_errors.append("Parameter type not provided")

            feature_extractor_columns.append(
                FeatureExtractorColumn(
                    name = arg_map['name'],
                    data_type = arg_map['type'],
                    description = arg_map['description'],
                    errors = param_errors
                )
            )

        feature_extractor_metadata = FeatureExtractorMetadata(
            feature_extractor_name = extractor.name,
            feature_extractor_description = function_description,
            feature_extractor_columns = feature_extractor_columns,
            errors = errors
        )

        extractors.append(feature_extractor_metadata.to_json())

    return extractors

if __name__ == '__main__':
    import traceback

    try:
        print_result(generate_metadata())
    except Exception:
        print_result(json.dumps(dict(errors=[traceback.format_exc()])))
        exit(1)
