"""Command-line interface for godkjenn.
"""

import logging
from pathlib import Path
import sys

from exit_codes import ExitCode

import click
import godkjenn.config
import godkjenn.plugins
from godkjenn.version import __version__

log = logging.getLogger(__name__)


@click.group()
@click.option('--verbosity',
              default='WARNING',
              help="The logging level to use.",
              type=click.Choice([name
                                 for lvl, name in sorted(logging._levelToName.items())
                                 if lvl > 0],
                                case_sensitive=True))
@click.version_option(version=__version__)
def cli(verbosity):
    logging_level = getattr(logging, verbosity)
    logging.basicConfig(level=logging_level)


@cli.command()
@click.option('--config', help='Config file to load', type=Path)
@click.option('--root-dir', help='Root directory', type=Path)
@click.argument('test_id')
def accept(config, root_dir, test_id):
    if config is not None:
        config = godkjenn.config.load_config(config)
    else:
        config = godkjenn.config.default_config(root_dir)

    vault = godkjenn.plugins.get_vault(config)

    try:
        rx = vault.get_received(test_id)
    except KeyError:
        log.error('No received data for {}'.format(test_id))
        return ExitCode.DATA_ERR

    vault.put_accepted(test_id, rx)
    vault.delete_received(test_id)

    return ExitCode.OK


def main(argv=None):
    return cli(argv)


if __name__ == '__main__':
    sys.exit(main())
