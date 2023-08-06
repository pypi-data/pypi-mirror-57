import click
import json
import sys
import traceback

from lhub_extractors import util
from lhub_extractors import feature_extractor


def run_extractor(entrypoint_fn):
    node_output_table = []
    node_metadata = {}

    for data in sys.stdin.readlines():
        as_dict = json.loads(data)

        if 'node_metadata' in as_dict:
            node_metadata = as_dict['node_metadata']

        if 'row' in as_dict:
            row = as_dict['row']
            node_output_table.append(row)

    try:
        result = entrypoint_fn(node_metadata, node_output_table)

        if result:
            util.print_result(json.dumps(result))
    except Exception:
        util.print_error(traceback.format_exc(), data=as_dict)

@click.command()
@click.option("--entrypoint", "-e", required=True)
def main(entrypoint):
    errors = util.import_workdir()
    if errors:
        util.hard_exit_from_instantiation(str(errors[0]))
    entrypoint_fn = feature_extractor.all().get(entrypoint).function
    assert entrypoint_fn is not None
    run_extractor(entrypoint_fn)

if __name__ == "__main__":
    main()
