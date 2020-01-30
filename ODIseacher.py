import subprocess
import os
import requests
import time
from hurry.filesize import size
search = ""
search = raw_input("Enter search term: ")
search2 = ' cat Scans/*'  + ' | grep -i ' + search
with open('scans.txt', 'w') as file_obj:
    subprocess.call(search2, shell=True, stdout=file_obj, stderr=file_obj)


fileHandler = open ("scans.txt", "r")
listOfLines = fileHandler.readlines()
fileHandler.close()

for line in listOfLines:
    try:
        response = requests.head(line.strip(), timeout=5)
    except:
        response = "UNKNOWN"
    if "https://" in line.strip():
        url1 = line.strip().replace("https://", "http://")
        #print url1
    else:
        url1 = line.strip()
        #print url1
    if response != "UNKNOWN":
        size2 = size(int(response.headers['Content-Length'])) + "b"
    else:
        size2 = "UNKNOWN"
    url2=url1.split("http://",1)[1]
    #print url2
    url3=url2.split("/",1)[0]
    #print url3
    time.sleep(0.1)
    fileHandler2 = open ("downloadspeedtest.txt", "r")
    listOfLines2 = fileHandler2.readlines()
    fileHandler2.close()
    for line2 in listOfLines2:
        if url3 == line2.strip().rstrip().split(' ', 1)[0]:
            speed = line2.strip().rstrip().split(' ', 1)[1]
    print line.strip() + ' ' + size2 + " " + "~" + speed
