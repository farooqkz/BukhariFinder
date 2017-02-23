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

from supybot.test import *


class BukhariFinderTestCase(PluginTestCase):
    plugins = ('BukhariFinder',)


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
