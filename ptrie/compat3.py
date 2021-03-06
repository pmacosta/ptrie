# compat3.py
# Copyright (c) 2013-2019 Pablo Acosta-Serafini
# See LICENSE for details
# pylint: disable=C0111,W0122,W0613,W0706


###
# Function
###
def _readlines(fname, fpointer1=open, fpointer2=open):  # pragma: no cover
    """Read all lines from file."""
    # fpointer1, fpointer2 arguments to ease testing
    try:
        with fpointer1(fname, "r") as fobj:
            return fobj.readlines()
    except UnicodeDecodeError:  # pragma: no cover
        with fpointer2(fname, "r", encoding="utf-8") as fobj:
            return fobj.readlines()
    except:  # pragma: no cover
        raise
