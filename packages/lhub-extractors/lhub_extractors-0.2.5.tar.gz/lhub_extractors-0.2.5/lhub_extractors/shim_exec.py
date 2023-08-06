import click
import json
import sys

from lhub_extractors import util
from lhub_extractors import feature_extractor

def run_extractor(entrypoint_fn):

    output_table = []
    node_metadata = {}

    print("running")

    for data in sys.stndin.readlines():
        as_dict = json.loads(data)

        if as_dict.has_key['node_metadata']:
            node_metadata = as_dict['node_metadata']

        if as_dict.has_key['row']:
            row = as_dict['row']
            output_table.append(row)

    print(output_table)

    util.print_result(output_table)
    # print(node_metadata)


@click.command()
@click.option("--entrypoint", "-e", required=True)
def main(entrypoint):
    print("hello")
    errors = util.import_workdir()
    if errors:
        print("error")
        #util.hard_exit_from_instantiation(str(errors[0]))
    print(feature_extractor.all())
    entrypoint_fn = feature_extractor.all().get(entrypoint).function
    assert entrypoint_fn is not None
    run_extractor(entrypoint_fn)


if __name__ == "__main__":
    entrypoint = "temp_extractor.feature_extractor_func"
    errors = util.import_workdir()
    if errors:
        # util.hard_exit_from_instantiation(str(errors[0]))
        print(errors)
        print("exit")

    print(feature_extractor.all())

    for f in feature_extractor.all().values():
        print(f.entrypoint)

    extractor = feature_extractor.all().get(entrypoint)
    print(extractor)
    if extractor is not None:
        entrypoint_fn = extractor.function
        assert entrypoint_fn is not None
        run_extractor(entrypoint_fn)