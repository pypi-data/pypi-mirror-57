"""Simple file-system based implementation of a vault.
"""

from enum import Enum
from pathlib import Path


class FSVault:
    """File-system implementation of a vault.

    This just keeps accepted data in files with the "accepted" suffix and received data in files suffixed with
    "received". Id's in this vault are simply paths.

    This assumes it has complete control over the files under `root_directory`.

    Args:
        root_path: The root directory under which this will store received and accepted data.
    """

    def __init__(self, root_path: Path):
        self._root_path = root_path

    @property
    def root_path(self):
        "Root path of the vault."
        return self._root_path

    def get_accepted(self, path):
        """Get the current accepted value at `path`.

        Args:
            path: Path to the file containing the value.

        Returns: A bytes object with the file's contents.

        Raises:
            KeyError: `path` does not exist.
        """
        return self._get(path, _Kind.accepted)

    def put_accepted(self, path, value):
        self._put(path, _Kind.accepted, value)

    def get_received(self, path):
        """Get the current received value at `path`.

        Args:
            path: Path to the file containing the value.

        Returns: A bytes object with the file's contents.

        Raises:
            KeyError: Received `path` does not exist.
        """

        return self._get(path, _Kind.received)

    def put_received(self, path, value):
        self._put(path, _Kind.received, value)

    def delete_received(self, path):
        p = self._full_path(path, _Kind.received)
        if p.exists():
            p.unlink()

    def _full_path(self, path, kind):
        return self._root_path / '{}.{}'.format(path, kind.value)

    def _get(self, path, kind):
        full_path = self._full_path(path, kind)

        if not full_path.exists():
            raise KeyError('no {} record with id={}'.format(kind, path))

        with full_path.open(mode='rb') as handle:
            return handle.read()

    def _put(self, path, kind, value):
        full_path = self._full_path(path, kind)
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with full_path.open(mode='wb') as handle:
            handle.write(value)


class _Kind(Enum):
    accepted = 'accepted'
    received = 'received'


def plugin(full_config, plugin_config):
    """Vault plugin for FSVault.

    Args:
        full_config: The full godkjenn config dict.
        plugin_config: The sub-config for the plugin.

    Returns: A new FSVault instance.
    """
    # TODO: We should give users a config option for changing .godkjenn to something else.
    return FSVault(root_path=Path(full_config['root_dir']) / '.godkjenn')
