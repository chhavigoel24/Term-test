file = open("part2.txt","r+")
strg=file.read(10)
print(strg)
pos=file.tell()
print("current file position is :" ,pos)
file.seek(20,0)
strg1=file.read(5)
print(strg1)
new_pos=file.tell()
print("current file position is : ",new_pos)
file.seek(0)
strg1=file.read()
print(strg1.strip())





