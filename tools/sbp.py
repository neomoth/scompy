import os
print("Where is the binary located. Make sure to include the name of the binary. (ex: /bin/executable.exe)\n")
path = input(">> ")
f = open("./tools/binpath", "w")
f.write(path)
f.close()
print("Successfully saved binary path as {}".format(path))
