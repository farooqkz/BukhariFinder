####
#
#    A limnoria plugin which you can get Sahih-Bukhari Hadiths
#    Copyright (C) 2017 FarooghKZ <farooghkz@openmailbox.org>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details(see LICENSE or GPL3 if
#        available).
#
###

import supybot.conf as conf
import supybot.registry as registry
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('BukhariFinder')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified themself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('BukhariFinder', True)


BukhariFinder = conf.registerPlugin('BukhariFinder')
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(BukhariFinder, 'someConfigVariableName',
#     registry.Boolean(False, _("""Help for someConfigVariableName.""")))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
