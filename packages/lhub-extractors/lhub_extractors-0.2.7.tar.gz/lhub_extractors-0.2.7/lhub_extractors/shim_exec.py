import click
import json
import sys

from lhub_extractors import util
from lhub_extractors import feature_extractor

def run_extractor(entrypoint_fn):

    output_table = []
    node_metadata = {}

    for data in sys.stdin.readlines():
        as_dict = json.loads(data)

        if as_dict.has_key['node_metadata']:
            node_metadata = as_dict['node_metadata']

        if as_dict.has_key['row']:
            row = as_dict['row']
            output_table.append(row)

    util.print_result(output_table)

@click.command()
@click.option("--entrypoint", "-e", required=True)
def main(entrypoint):
    errors = util.import_workdir()
    if errors:
        print("error")
        #util.hard_exit_from_instantiation(str(errors[0]))
    entrypoint_fn = feature_extractor.all().get(entrypoint).function
    assert entrypoint_fn is not None
    run_extractor(entrypoint_fn)
