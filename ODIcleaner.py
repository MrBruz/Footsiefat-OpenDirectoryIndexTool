import glob
import os
files = glob.glob("Scans/*.txt")
for x in files:
  statinfo = os.stat(x)
  print(x + " " + str(statinfo.st_size))
  if statinfo.st_size == 0:
    os.remove(x)
