import vakt
from vakt import __version__


def test_version():
    assert '1.4.0' == __version__


def test_version_info():
    assert (1, 4, 0) == vakt.version_info()
