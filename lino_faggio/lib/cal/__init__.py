# -*- coding: UTF-8 -*-
# Copyright 2013-2014 Luc Saffre
# License: BSD (see file COPYING for details)

from lino.modlib.cal import Plugin


class Plugin(Plugin):

    extends_models = ['Event', 'Room']
