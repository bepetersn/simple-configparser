
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


class FilePaddedForIteration:
    """
    A class whose primary interface is the
    __iter__ method. When accessed this way,
    it will act like a file, incorporating
    the padding with which it was
    initialized at the top of file.

    """

    def __init__(self, padding, file):
        self._file = file
        self._padding = padding

    def __iter__(self):
        if self._file.tell() == 0:
            padding_lines = self._padding.split()
            for line in padding_lines:
                yield line

        with open(self._file.name, encoding='utf-8', mode='rt') as f:
           for line in self._file.readlines():
                yield line





