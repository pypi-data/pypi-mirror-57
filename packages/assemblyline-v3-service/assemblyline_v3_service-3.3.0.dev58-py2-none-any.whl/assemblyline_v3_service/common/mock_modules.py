import sys

from types import ModuleType


class MockAssemblylineAlCommonTransport(ModuleType):
    def __init__(self):
        super(MockAssemblylineAlCommonTransport, self).__init__('assemblyline.al.common.transport')

        import assemblyline_v3_service.common.transport.local
        self.local = assemblyline_v3_service.common.transport.local
        self.local.__name__ = 'assemblyline.al.common.transport.local'


class MockAssemblylineAlService(ModuleType):
    def __init__(self):
        super(MockAssemblylineAlService, self).__init__('assemblyline.al.service')

        import assemblyline_v3_service.common.base
        self.base = assemblyline_v3_service.common.base
        self.base.__name__ = 'assemblyline.al.service.base'


class MockAssemblylineAlCommon(ModuleType):
    def __init__(self):
        super(MockAssemblylineAlCommon, self).__init__('assemblyline.al.common')

        self.transport = MockAssemblylineAlCommonTransport()
        self.transport.__name__ = 'assemblyline.al.common.transport'

        import assemblyline_v3_service.common.result
        self.result = assemblyline_v3_service.common.result
        self.result.__name__ = 'assemblyline.al.common.result'

        import assemblyline_v3_service.common.mock_forge
        self.forge = assemblyline_v3_service.common.mock_forge
        self.forge.__name__ = 'assemblyline.al.common.forge'


class MockAssemblylineCommon(ModuleType):
    def __init__(self):
        super(MockAssemblylineCommon, self).__init__('assemblyline.al')

        from assemblyline_v3_service.common import str_utils
        self.charset = str_utils
        self.charset.__name__ = 'assemblyline.common.charset'

        from assemblyline_v3_service.common import mock_forge
        self.forge = mock_forge
        self.forge.__name__ = 'assemblyline.common.forge'


class MockAssemblylineAl(ModuleType):
    def __init__(self):
        super(MockAssemblylineAl, self).__init__('assemblyline.al')

        self.common = MockAssemblylineAlCommon()
        self.common.__name__ = 'assemblyline.al.common'

        self.service = MockAssemblylineAlService()
        self.service.__name__ = 'assemblyline.al.service'

        import assemblyline_v3_service.common.install
        self.install = assemblyline_v3_service.common.install
        self.install.__name__ = 'assemblyline.al.install'


class MockAssemblyline(ModuleType):
    def __init__(self):
        super(MockAssemblyline, self).__init__('assemblyline')

        self.al = MockAssemblylineAl()
        self.al.__name__ = 'assemblyline.al'

        import assemblyline_v3_service.common as common

        from assemblyline_v3_service.common import str_utils
        common.charset = str_utils
        common.charset.__name__ = 'assemblyline.common.charset'
        self.common = common

        from assemblyline_v3_service.common import mock_forge
        common.forge = mock_forge
        common.forge.__name__ = 'assemblyline.common.forge'

        from assemblyline_v3_service.common import hexdump
        common.hexdump = hexdump
        common.hexdump.__name__ = 'assemblyline.common.hexdump'

        from assemblyline_v3_service.common import reaper
        common.reaper = reaper
        common.reaper.__name__ = 'assemblyline.common.reaper'

        from assemblyline_v3_service.common import timeout
        common.timeout = timeout
        common.timeout.__name__ = 'assemblyline.common.timeout'

        # TODO: for testing only
        from assemblyline_v3_service.common import identify
        common.identify = identify
        common.identify.__name__ = 'assemblyline.common.identify'


class MockAssemblyline2AlCommon(ModuleType):
    def __init__(self):
        super(MockAssemblyline2AlCommon, self).__init__('assemblyline.al.common')

        from assemblyline_v3_service.common import heuristics
        self.heuristics = heuristics
        self.heuristics.__name__ = 'assemblyline.al.common.heuristics'

        from assemblyline_v3_service.common import mock_forge
        self.forge = mock_forge
        self.forge.__name__ = 'assemblyline.al.common.forge'


class MockAssemblyline2Al(ModuleType):
    def __init__(self):
        super(MockAssemblyline2Al, self).__init__('assemblyline.al')
        self.common = MockAssemblyline2AlCommon()
        self.common.__name__ = 'assemblyline.al.common'


class MockAssemblyline2(ModuleType):
    def __init__(self):
        super(MockAssemblyline2, self).__init__('assemblyline')
        self.al = MockAssemblyline2Al()
        self.al.__name__ = 'assemblyline.al'


def modules1():
    mock_al = MockAssemblyline()
    sys.modules['assemblyline'] = mock_al
    sys.modules['assemblyline.al'] = mock_al.al
    sys.modules['assemblyline.al.common'] = mock_al.al.common
    sys.modules['assemblyline.al.common.forge'] = mock_al.al.common.forge
    sys.modules['assemblyline.al.common.result'] = mock_al.al.common.result
    sys.modules['assemblyline.al.common.transport'] = mock_al.al.common.transport
    sys.modules['assemblyline.al.common.transport.local'] = mock_al.al.common.transport.local
    sys.modules['assemblyline.al.service'] = mock_al.al.service
    sys.modules['assemblyline.al.service.base'] = mock_al.al.service.base
    sys.modules['assemblyline.al.install'] = mock_al.al.install
    sys.modules['assemblyline.common'] = mock_al.common
    sys.modules['assemblyline.common.charset'] = mock_al.common.charset
    sys.modules['assemblyline.common.forge'] = mock_al.common.forge
    sys.modules['assemblyline.common.hexdump'] = mock_al.common.hexdump
    sys.modules['assemblyline.common.identify'] = mock_al.common.identify
    sys.modules['assemblyline.common.reaper'] = mock_al.common.reaper
    sys.modules['assemblyline.common.timeout'] = mock_al.common.timeout



def modules2():
    mock_al = MockAssemblyline2()
    sys.modules['assemblyline'] = mock_al
    sys.modules['assemblyline.al'] = mock_al.al
    sys.modules['assemblyline.al.common'] = mock_al.al.common
    sys.modules['assemblyline.al.common.heuristics'] = mock_al.al.common.heuristics
    sys.modules['assemblyline.al.common.forge'] = mock_al.al.common.forge
