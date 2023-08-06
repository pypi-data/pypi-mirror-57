import pytest

from remediation.data_generators import CM11Generator
from remediation.utils import Singleton


@pytest.fixture()
def create_cm11_object():
    return CM11Generator()


def test_cm11_generator_is_singleton(create_cm11_object):
    assert isinstance(create_cm11_object, Singleton)


@pytest.mark.skip(
    reason='not required..otherwise it discharges the generator')
def test_aaa(create_cm11_object):
    assert len(create_cm11_object.words) == \
            len(list(create_cm11_object.generate_word))
