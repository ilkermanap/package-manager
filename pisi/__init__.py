# -*- coding: utf-8 -*-
#
# Copyright (C) 2016-2017, Aquila Nipalensis
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

# PiSi version

import os
import sys
import atexit
import logging
import logging.handlers
import imp

__version__ = "3.0.1"

__all__ = [ 'api', 'configfile', 'db']

# FIXME: Exception shadows builtin Exception. This is no good.
class Exception(Exception):
    """Class of exceptions that must be caught and handled within PiSi"""
    def __str__(self):
        s = ''
        for x in self.args:
            if s != '':
                s += '\n'
            s += str(x)
        return s

class Error(Exception):
    """Class of exceptions that lead to program termination"""
    pass

import pisi.api
import pisi.config
import pisi.context as ctx

def init_logging():
    log_dir = os.path.join(ctx.config.dest_dir(), ctx.config.log_dir())
    if os.access(log_dir, os.W_OK) and "distutils.core" not in sys.modules:
        handler = logging.handlers.RotatingFileHandler('%s/pisi.log' % log_dir)
        formatter = logging.Formatter('%(asctime)-12s: %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        ctx.log = logging.getLogger('pisi')
        ctx.log.addHandler(handler)
        ctx.loghandler = handler
        ctx.log.setLevel(logging.DEBUG)

def _cleanup():
    """Close the database cleanly and do other cleanup."""
    ctx.disable_keyboard_interrupts()
    if ctx.log:
        ctx.loghandler.flush()
        ctx.log.removeHandler(ctx.loghandler)

    filesdb = pisi.db.filesdb.FilesDB()
    if filesdb.is_initialized():
        filesdb.close()

    if ctx.build_leftover and os.path.exists(ctx.build_leftover):
        os.unlink(ctx.build_leftover)

    ctx.ui.close()
    ctx.enable_keyboard_interrupts()

# Hack for pisi to work with non-patched Python. pisi needs
# lots of work for not doing this.
imp.reload(sys)
sys.setdefaultencoding('utf-8')

atexit.register(_cleanup)

ctx.config = pisi.config.Config()
init_logging()