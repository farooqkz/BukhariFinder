###
# Copyright (c) 2016, FarooghKZ
# All rights reserved.
#
# This is free software under GPL3+
# WITHOUT ANY WARRENTY FROM MAIN AUTHOR BY DEFAULT!
# for license see LICENSE
###

import supybot.conf as conf
import supybot.registry as registry
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('BukhariFinder')
except:
    _ = lambda x: x

def configure(advanced):
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('BukhariFinder', True)

BukhariFinder = conf.registerPlugin('BukhariFinder')

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79: