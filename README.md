# Footsiefat-OpenDirectoryIndexTool
It allows for searching through multiple OD's at once and includes file size and download speed in preview, also includes feature to get more OD's from a google search! 



Requirments...
Well actually I dont know them all, but you need the default python for a start.

**-Linux**

-Default python

-curl

**install the following with pip**

-bs4

-shlex

-hashlib?

-hurry.filesize

If there are any others please let me know in issues.


How to use:


**Do you have a list of open directories that can be copyed to a txt file? if so copy them to data.txt then run the following**

python ODIwebsitechecker.py

python ODIwebsiteindexer.py (If this spits out a yellow warning msg saying something failed and it will try again in N seconds please hit ESC to skip the directorie)

python ODIdownloadspeedtest.py

python ODIcleaner.py


**Once you have done this you can now discover new directories with ODIgooglesearcher.py but this is again optional**

When it prompts you to enter a search term use one of the following:

For videos/movies/tvshows :

intext:"Search Term" intitle:"index.of" +(wmv|mpg|avi|mp4|mkv|mov) -inurl:(jsp|pl|php|html|aspx|htm|cf|shtml)

Images :

intext:"Search Term" intitle:"index.of./" (bmp|gif|jpg|png|psd|tif|tiff) -inurl:(jsp|pl|php|html|aspx|htm|cf|shtml)

Music :

intext:"Search Term" intitle:"index.of./" (ac3|flac|m4a|mp3|ogg|wav|wma) -inurl:(jsp|pl|php|html|aspx|htm|cf|shtml)

Books :

intitle:"Search Term" (pdf|epub|mob) "name or title" -inurl:(jsp|pl|php|html|aspx|htm|cf|shtml)


**Replace "Search Term" with your search term for the media you want to find.**

Once this has run(and remember to hit ESC if any yellow warning msgs appear saying it cannot do something, trying again in N seconds) run the following...

python ODIcleaner.py



**Now you can run the search tool!**

python ODIsearcher.py (remember to only use one word as a search term otherwise this breaks)

This includes the file sizes and average download speed!


**ENJOY GUYS, and remember report any problems or improvments to issues**
