from subprocess import call
from os import listdir
from os.path import isfile, join
#call(["rm -r generated/*"], shell=True)
call(["python", "generate_benchmarks.py"])
files = [f for f in listdir("generated") if isfile(join("generated", f))]
#for f in files:
    #call(["encorec","-I","..", "-o", "generated/" + f[:-4], "generated/" + f])

for f in files:
    print(f)
    call(["generated/" + f[:-4]])
