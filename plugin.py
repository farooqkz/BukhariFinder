###
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

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import json
import random
import os

try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('BukhariFinder')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


class BukhariFinder(callbacks.Plugin):
    """Get Sahih Bukhari Hadiths in IRC"""
    threaded = True
    db = None
    def __init__(self, irc):
        self.__parent = super(BukhariFinder, self)
        self.__parent.__init__(irc)
        with open('sahih_bukhari.json') as fs:
            self.db = json.loads(fs.read())

    def rbukhari(self, irc, msg, args):
        """takes no argument

        Selects a random hadith and returns it
        """
        
        hadith = random.choice(self.db[random.choice(tuple(self.db.keys()))])
        t = ' '.join(hadith['info'].split(',')).split()
        
        irc.reply(':'.join((t[1], t[3], t[5])) + ', ' + hadith['text'] + hadith['by'])

    rbukhari = wrap(rbukhari)

    def bukhari(self, irc, msg, args, book_no, hadith_no):
        """<book_no> <hadith_no>

        Gets and returns hadith number <hadith_no> in book number
        <book_no>
        """
         
        #getting book key by book number
        try:
            book_key = None
            for k in self.db.keys():
                if k.startswith(str(book_no) + '.'):
                    book_key = k
                    break
        
            hadith = self.db[book_key][hadith_no - 1]
            t = ' '.join(hadith['info'].split(',')).split()
            t = ':'.join((t[1], t[3], t[5]))
            irc.reply(t + ', ' + hadith['text'] + hadith['by'])
        except KeyError:
            irc.reply("Book number " + str(book_no) + " not found!")
        except IndexError:
            irc.reply("Hadith number " + str(hadith_no) + " not found!")
    bukhari = wrap(bukhari, ['int', 'int'])


Class = BukhariFinder


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
