import shlex
import subprocess
import os
import hashlib
import time

#Load urls
fileHandler = open ("data.txt", "r")
listOfLines = fileHandler.readlines()
fileHandler.close()

# Tokenize the shell command
# cmd will contain  ["ping","-c1","google.com"]

cmd="google.com"

os.remove("out1.txt")
os.remove("out3.txt")

def ping( ip, ip2 ):
        cmd=shlex.split("ping -c1 " + ip)
        try:
            output = subprocess.check_output(cmd)
        except subprocess.CalledProcessError,e:
            #Will print the command failed with its exit status
            print "The IP {0} is NotReacahble".format(cmd[-1])
        else:
            print "The IP {0} is Reachable".format(cmd[-1])
            text_file = open("out1.txt", "a")
            text_file.write(ip)
            text_file.write(os.linesep)
            text_file.close()
            text_file = open("out3.txt", "a")
            text_file.write(ip2)
            text_file.write(os.linesep)
            text_file.close()
            time.sleep(1)


for line in listOfLines:
    url1=line.strip().split("http://",1)[1]
    url2=url1.split("/",1)[0]
    ping(url2, line.strip())


output_file_path = "out2.txt"
input_file_path = "out1.txt"
completed_lines_hash = set()
output_file = open(output_file_path, "w")
for line in open(input_file_path, "r"):
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
output_file.close()
