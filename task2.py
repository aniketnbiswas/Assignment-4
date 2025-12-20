file="output.txt"

fh=open(file,'wt')
x= input("Enter text to write to the file: ")
fh.write(f"{x}\n")
print(f"Data successfully written to {file}")
fh.close()

print("==============================")

fh1=open(file,'at')
y=input("Enter additional text to append: ")
print(f"Data successfully appended")
fh1.write(y)
fh1.close()

print("==============================")

fh2=open(file,'rt')
lines= fh2.readlines()
print("Final content of output.txt: ")
for line in lines:
    print(line.rstrip())
fh2.close()
print("==============================")