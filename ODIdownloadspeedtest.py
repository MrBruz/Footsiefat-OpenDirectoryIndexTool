import subprocess
import os
import shlex
import time
import sys
from hurry.filesize import size
import re


def fl(fl):
    with open(fl, "r") as f:
        first = f.readline().rstrip()     # Read the first line.
    return first

def ll(ll):
    with open('log.txt', "r") as f:
        f.seek(-2, os.SEEK_END)     # Jump to the second last byte.
        while f.read(1) != b"\n":   # Until EOL is found...
            f.seek(-2, os.SEEK_CUR) # ...jump back the read byte plus one more.
        last = f.readline()
        return last


try:
    f = open("downloadspeedtest.txt")
    os.remove("downloadspeedtest.txt")
except IOError:
    print("File not accessible" + '\n')


list = os.listdir("Scans")
for item in list:
    print(item)
    scan = 'Scans/' + item
    #print scan
    first = fl(scan)# Read the first line.
    print first
    down = "curl " + "\"" + first + "\"" + " --max-time 20  -o downloadtest.txt"
    #print down
    with open('log.txt', 'w') as file_obj:
        subprocess.call(down, shell=True, stdout=file_obj, stderr=file_obj)
        last = ll('log.txt')     # Read last line.
        print last.rstrip()
        #print ord(last[:1])
        if ord(last[:1]) == 13:

            out = "ERROR_DOWNLOADING"
        else:
            if last == "curl: (28) Connection timed out after 20000 milliseconds":
                out = "ERROR_CANNOT_CNT_2_SVR"
            speed = last.split("with ",1)[1].split(" out",1)[0]
            if speed == '0 bytes received\n':
                out = "ERROR_CANNOT_DOWNLOAD"
            else:
                out = size(int(speed) / 10) + "bps"
        if last == "curl: (7) Couldn't connect to server":
            out = "ERROR_CANNOT_CNT_2_SVR"
        if last == "":
            out = "ERROR_ETC"
        print out
        if "https://" in first:
            url1 = first.replace("https://", "http://")
        else:
            url1 = first
        url2=url1.split("http://",1)[1]
        url3=url2.split("/",1)[0]
        print url3
        text_file = open("downloadspeedtest.txt", "a")
        text_file.write(url3 + " " + out)
        text_file.write(os.linesep)
        text_file.close()
        print "\n"
