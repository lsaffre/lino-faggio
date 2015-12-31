# -*- coding: UTF-8 -*-
# Copyright 2012-2015 Luc Saffre
# License: BSD (see file COPYING for details)

from lino.projects.std.settings import *

from lino_voga import SETUP_INFO


class Site(Site):
    version = SETUP_INFO['version']
    verbose_name = "Lino Voga"
    url = SETUP_INFO['url']

    #~ help_url = "http://lino.saffre-rumma.net/az/index.html"

    migration_class = 'lino_voga.migrate.Migrator'

    userdocs_prefix = 'voga.'

    user_profiles_module = 'lino_voga.projects.roles'

    demo_fixtures = 'std minimal_ledger demo demo_bookings buche voga demo2'.split()

    languages = 'en de et'

    show_internal_field_names = True

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.gfks'
        # yield 'lino.modlib.system'
        yield 'lino.modlib.users'
        yield 'lino.modlib.countries'
        yield 'lino_voga.lib.contacts'
        yield 'lino.modlib.lists'
        yield 'lino.modlib.beid'

        yield 'lino_voga.lib.cal'
        yield 'lino.modlib.extensible'
        yield 'lino_voga.lib.rooms'

        yield 'lino.modlib.products'
        yield 'lino_cosi.lib.accounts'
        yield 'lino_cosi.lib.ledger'
        yield 'lino_cosi.lib.vat'
        #~ yield 'lino_cosi.lib.declarations'
        #~ yield 'lino_cosi.lib.sales'
        yield 'lino_cosi.lib.auto.sales'
        yield 'lino_cosi.lib.finan'
        yield 'lino_cosi.lib.sepa'

        yield 'lino_voga.lib.courses'

        #~ yield 'lino.modlib.households'
        yield 'lino.modlib.notes'
        yield 'lino.modlib.uploads'
        #~ yield 'lino.modlib.cal'

        yield 'lino.modlib.outbox'
        yield 'lino.modlib.excerpts'
        #~ yield 'lino.modlib.pages'
        #~ yield 'lino_cosi.lib.courses'
        yield 'lino_voga'

        # yield 'lino.modlib.appypod'
        yield 'lino.modlib.export_excel'

    def get_admin_main_items(self, ar):
        yield self.modules.courses.DraftCourses
        # yield self.modules.courses.ActiveCourses

    def setup_plugins(self):
        """
        Change the default value of certain plugin settings.
       
        """
        self.plugins.extensible.configure(calendar_start_hour=9)
        self.plugins.extensible.configure(calendar_end_hour=21)
        self.plugins.vat.configure(default_vat_class='exempt')
        self.plugins.ledger.configure(start_year=2015)
        super(Site, self).setup_plugins()
