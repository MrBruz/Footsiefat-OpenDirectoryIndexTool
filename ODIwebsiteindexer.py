import shlex
import subprocess
import os

fileHandler = open ("out3.txt", "r")
listOfLines = fileHandler.readlines()
fileHandler.close()

def index(ip):
    os.system('./OpenDirectoryDownloader --url ' + ip + ' --quit')


for line in listOfLines:
    index(line.strip())
