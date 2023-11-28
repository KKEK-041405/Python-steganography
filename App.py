import read
import write
print("Choose the operation: ")
print("1.write msg")
print("2.Read msg")
opt = input()
if(opt == '1'):write.write()
else: read.read()