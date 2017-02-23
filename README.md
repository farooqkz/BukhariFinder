#Get Sahih Bukhari Hadiths in IRC
##Introduction
Thanks to God and Peace be upon Muhammad and Jesus Christ and anyone following them in the right way.

It's a limnoria plug-in which uses __this_date_base__ to provide Sahih Bukhari hadiths in IRC.

currently it has two commands:
`!rbukhari' - Selects and returns a random hadith
`!bukhari \<book\_no\> \<hadith\_no\>' - Selects hadith number \<hadith\_no\> in the book \<book\_no\>

A hadith will be returned in this format:
 VolNo:BookNo:HadithNo, Hadith text. narrator
##Problem/Bugs
It loads the json file directly to memory, all of it!this means about 4MB memory usage when the plug-in is loaded.
##Todo
 [ ] !search command
 [ ] fixing the problem(maybe using sqlite3?)

