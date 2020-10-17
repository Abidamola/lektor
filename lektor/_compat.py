# -*- coding: utf-8 -*-
"""
    lektor._compat
    ~~~~~~~~~~~~~~

    Some py2/py3 compatibility support based on a stripped down
    version of six so we don't have to depend on a specific version
    of it.

    Taken from jinja2/_compat.py
"""
# pylint: disable=invalid-name, import-error, unused-import, undefined-variable, reimported
import sys


PY2 = sys.version_info[0] == 2
_identity = lambda x: x


if PY2:
    unichr = unichr  # pylint: disable=self-assigning-variable  # noqa
    text_type = unicode  # noqa
    range_type = xrange  # noqa
    string_types = (str, unicode)  # noqa
    integer_types = (int, long)  # noqa

    iterkeys = lambda d: d.iterkeys()
    itervalues = lambda d: d.itervalues()
    iteritems = lambda d: d.iteritems()

    from cStringIO import StringIO as BytesIO, StringIO
    import Queue as queue  # noqa

    NativeStringIO = BytesIO

    exec(  # pylint: disable=exec-used
        "def reraise(tp, value, tb=None):\n raise tp, value, tb"
    )


else:
    unichr = chr
    range_type = range
    text_type = str
    string_types = (str,)
    integer_types = (int,)

    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())

    from io import BytesIO, StringIO
    import queue  # noqa

    NativeStringIO = StringIO

    def reraise(tp, value, tb=None):
        if value.__traceback__ is not tb:
            raise value.with_traceback(tb)
        raise value
