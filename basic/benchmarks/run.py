from subprocess import call
from os import listdir
from os.path import isfile, join
import sys
#call(["rm -r generated/*"], shell=True)
call(["python", "generate_benchmarks.py"])
files = [f for f in listdir("generated") if isfile(join("generated", f)) and f[-4:] == ".enc"]
files.sort()
for f in files:
    call(["encorec","-I","..", "-o", "generated/" + f[:-4], "generated/" + f])
names = ["Add Contains", "Add Remove Mixed", "Add Remove", "Add Same", "Add", "Few Add Contains"]
i = 0
for f in files:
    if i % 4 == 0:
        print("")
        sys.stdout.write(names[i / 4])
        sys.stdout.flush()
    sys.stdout.write(" & ")
    sys.stdout.flush()
    call(["generated/" + f[:-4]])
    i += 1
print("")
print("")
