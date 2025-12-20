import os
file="sample.txt"
if os.path.exists(file):
    sam=open(file,'rt')
    lines=sam.readlines()
    for line in lines:
        print(f"Line {lines.index(line)+1}: {line.rstrip()}")
    sam.close()
else:
    print(f"The file {file} was not found")
