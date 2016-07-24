###
# Copyright (c) 2016, FarooghKZ
# All rights reserved.
#
# This is free software under GPL3+ WITHOUT ANY WARRENTY FROM MAIN AUTHOR 
# BY DEFAULT!
# for license see LICENSE
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Foo')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


HADITH_DB_PATH = "./sahih_bukhari_py_list.txt"

class BukhariFinder(callbacks.Plugin):
    """BukhariFinder let's your read sahih bukhari hadtihs using supybot"""
    threaded = True
    
    def __init__():
        self.__parent = super(Random, self)
        self.__parent.__init__(irc)
        global hadiths
        with open(HADITH_DB_PATH, 'wt') as fp:
            hadiths = eval(fp.read())
    
    def bukhari(self, irc, msg, args, no):
        """<no>
        
        Returns hadith <no>
        """
        try:
            rmsg = hadiths[no + 1].split('\n')
            for m in rmsg:
                m = m.encode('utf-8')
                while len(m) > 350:
                    splitPoint = m[0:351].rfind(' '.encode('utf-8'))
                    irc.reply([m[0:splitPoint].decode('utf-8').strip()])
                    m = m[splitPoint:]
        except IndexError:
            irc.reply("Wrong hadith No.!")

    bukhari = wrap(bukhari, ["int"])

Class = BukhariFinder


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
