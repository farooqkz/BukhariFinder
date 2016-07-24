###
# Copyright (c) 2016, FarooghKZ
# All rights reserved.
#
# This is free software under GPL3+ WITHOUT ANY WARRENTY FROM MAIN AUTHOR 
# BY DEFAULT!
# for license see LICENSE
###

"""
Foo: Baz
"""

import supybot
import supybot.world as world

# Use this for the version of this plugin.  You may wish to put a CVS keyword
# in here if you're keeping the plugin in CVS or some similar system.
__version__ = "0.0"

# XXX Replace this with an appropriate author or supybot.Author instance.
__author__ = supybot.Author('Faroogh Karimi Zadeh', 'shangul', 'farooghkz@openmailbox.org')

# This is a dictionary mapping supybot.Author instances to lists of
# contributions.
__contributors__ = {}

# This is a url where the most recent plugin package can be downloaded.
__url__ = 'GITHUB_REPO'

from . import config
from . import plugin
from imp import reload
# In case we're being reloaded.
reload(config)
reload(plugin)
# Add more reloads here if you add third-party modules and want them to be
# reloaded when this plugin is reloaded.  Don't forget to import them as well!

if world.testing:
    from . import test

Class = plugin.Class
configure = config.configure


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
