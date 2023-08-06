
from remediation.utils import Singleton


class MySing(Singleton):
    def __init__(self, instanceName):
        Singleton.__init__(self)
        self.instanceName = instanceName


def test_singleton_instance_has_unique_state():
    a = MySing('instance_a')
    b = MySing('instance_b')

    assert a.instanceName == b.instanceName
