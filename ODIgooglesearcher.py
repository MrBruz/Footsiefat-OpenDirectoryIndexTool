import requests
from bs4 import BeautifulSoup
import re
import os
import shlex
import subprocess
import hashlib
import time



search = raw_input("Search:")
results = 20 # valid options 10, 20, 30, 40, 50, and 100

os.remove("googlesearch.txt")

page = requests.get("https://www.google.com/search?q={}&num={}".format(search, results))
soup = BeautifulSoup(page.content, "html5lib")
links = soup.findAll("a")
for link in links :
    link_href = link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href:
        print link.get('href').split("?q=")[1].split("&sa=U")[0]
        text_file = open("googlesearch.txt", "a")
        text_file.write(link.get('href').split("?q=")[1].split("&sa=U")[0])
        text_file.write('\n')
        text_file.close()


#intext:"Avengers" intitle:"index.of" +(wmv|mpg|avi|mp4|mkv|mov) -inurl:(jsp|pl|php|html|aspx|htm|cf|shtml)

for i in range(1,5):
    readFile = open("googlesearch.txt")
    lines = readFile.readlines()
    readFile.close()
    w = open("googlesearch.txt",'w')
    w.writelines([item for item in lines[:-1]])
    w.close()



# PART TWO - CHECK WEBSITES STILL UP



#Load urls
fileHandler = open ("googlesearch.txt", "r")
listOfLines = fileHandler.readlines()
fileHandler.close()

# Tokenize the shell command
# cmd will contain  ["ping","-c1","google.com"]

cmd="google.com"


try:
    f = open("googlesearch1.txt")
    os.remove("googlesearch1.txt")
except IOError:
    print("File not accessible" + '\n')


try:
    f = open("googlesearch3.txt")
    os.remove("googlesearch3.txt")
except IOError:
    print("File not accessible" + '\n')


def ping( ip, ip2 ):
        cmd=shlex.split("ping -c1 " + ip)
        try:
            output = subprocess.check_output(cmd)
        except subprocess.CalledProcessError,e:
            #Will print the command failed with its exit status
            print "The IP {0} is NotReacahble".format(cmd[-1])
            print '\n'
        else:
            print "The IP {0} is Reachable".format(cmd[-1])
            print '\n'
            text_file = open("googlesearch1.txt", "a")
            text_file.write(ip)
            text_file.write(os.linesep)
            text_file.close()
            text_file = open("googlesearch3.txt", "a")
            text_file.write(ip2)
            text_file.write(os.linesep)
            text_file.close()
            time.sleep(1)


for line in listOfLines:
    if "https://" in line.strip():
        url1 = line.strip().replace("https://", "http://")
        print url1
    else:
        url1 = line.strip()
        print url1
    url2=url1.split("http://",1)[1]
    print url2
    url3=url2.split("/",1)[0]
    print url3
    ping(url3, line.strip())


output_file_path = "googlesearch2.txt"
input_file_path = "googlesearch1.txt"
completed_lines_hash = set()
output_file = open(output_file_path, "w")
for line in open(input_file_path, "r"):
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
output_file.close()


#PART THREE - INDEX TIME, YAYYYYYYYY

fileHandler = open ("googlesearch3.txt", "r")
listOfLines = fileHandler.readlines()
fileHandler.close()

def index(ip):
    os.system('./OpenDirectoryDownloader --url ' + ip + ' --quit')


for line in listOfLines:
    index(line.strip())
