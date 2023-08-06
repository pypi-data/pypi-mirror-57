"""Command-line interface for godkjenn.
"""

import logging
import sys
from functools import wraps
from pathlib import Path

import click
import godkjenn.config
import godkjenn.plugins
from exit_codes import ExitCode
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


def _configured(f):
    """Decorator for subcommands that get a config dict either from a config file
    or from the default config value.

    Usage:

        @cli.command()
        @configured
        def subcommand_name(config):
            ... use config dict ...
    """
    @click.option('--config', help='Config file to load', type=Path)
    @click.option('--root-dir', help='Root directory', type=Path)
    @wraps(f)
    def wrapper(config, root_dir, *args, **kwargs):
        if config is not None:
            config = godkjenn.config.load_config(config)
        else:
            config = godkjenn.config.default_config(root_dir)
        return f(config, *args, **kwargs)

    return wrapper


@cli.command()
@_configured
@click.argument('test_id')
def accept(config, test_id):
    """Accept the current received data for a test.
    """
    vault = godkjenn.plugins.get_vault(config)

    try:
        vault.accept(test_id)
    except KeyError:
        log.error('No received data for {}'.format(test_id))
        return ExitCode.DATA_ERR

    return ExitCode.OK


@cli.command()
@_configured
def accept_all(config):
    """Accept all received data for a configuration/root directory.
    """
    vault = godkjenn.plugins.get_vault(config)

    for test_id in vault.ids():
        try:
            vault.accept(test_id)
        except KeyError:
            # This just means there isn't any received data for the ID, just accepted.
            pass

    return ExitCode.OK


def main(argv=None):
    return cli(argv)


if __name__ == '__main__':
    sys.exit(main())
