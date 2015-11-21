
import io
import configparser


DEFAULT_PADDING = """
[DEFAULT]

"""


class SimpleConfigParser(configparser.RawConfigParser):
    """
    A subclass of configparser.RawConfigParser that
    has no sections, and instead loads the key-value
    pairs provided into the "DEFAULT" section.

    These pairs are also made accessible by calling
    `parser.items()`.

    """

    def _read(self, fp, fpname):
        return super(SimpleConfigParser, self)._read(
            FilePaddedForIteration(DEFAULT_PADDING, fp),
            fpname
        )

    def items(self, section=configparser._UNSET, raw=False, vars=None):
        return self.defaults()


class FilePaddedForIteration(io.FileIO):
    """
    A subclass of io.FileIO which should only
    be used by iterating over it directly. When
    accessed this way, it will incorporate the
    padding with which it was initialized.

    """

    def __init__(self, padding, file):
        super(FilePaddedForIteration, self).__init__(file.name, file.mode)
        self._padding = padding

    def __iter__(self):
        if self.tell() == 0:
            padding_lines = self._padding.split()
            for line in padding_lines:
                yield line

        for line in self.readlines():
            yield line





