afrom subprocess import call
from os import listdir
from os.path import isfile, join
import sys
#call(["rm -r generated/*"], shell=True)
call(["python", "generate_benchmarks.py"])
files = [f for f in listdir("generated") if isfile(join("generated", f)) and f[-4:] == ".enc"]
files.sort()
for f in files:
    call(["encorec",'-c',"-I","..", "-o", "generated/" + f[:-4], "generated/" + f])
names = ["Add Contains", "Add Remove Mixed", "Add Remove", "Add Same", "Add", "Few Add Contains"]
i = 0
for f in files:
    #if i % 4 == 0:
    #    print("")
    #    sys.stdout.write(names[i / 4])
    #    sys.stdout.flush()
    #sys.stdout.write(" & ")
    #sys.stdout.flush()
    timeout = 150
    exitcode = call(["timeout", str(timeout), "generated/" + f[:-4]]) # If timeout becomes necessary http://linux.die.net/man/1/timeout
    if exitcode == 124:
        print(f[:-4] + "total >" +str(timeout))
    i += 1
print("")
print("")
