import os
path = 'C:\DRIVERS'
print("All directories:")
print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("All files:")
print([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("All directories,files:")
print([name for name in os.listdir(path)])

print('Exist:', os.access('C:\DRIVERS', os.F_OK))
print('Readable:', os.access('C:\DRIVERS', os.R_OK))
print('Writable:', os.access('C:\DRIVERS', os.W_OK))
print('Executable:', os.access('C:\DRIVERS', os.X_OK))

#3

print("Exists?:")
path = 'C:\\test\\a.txt'
print(os.path.exists(path))
print("File name of the path:")
print(os.path.basename(path))
print("Dir name of the path:")
print(os.path.dirname(path))

#4
with open(r"C:\\test\\a.txt", 'r') as f:
    print("Number of lines: ", len(f.readlines()))

#5
e = [1, 2, 3, 4, 5, 6, 7]
with open('C:\\test\\b.txt', "w") as mf:
        for i in e:
                mf.write("%s\n" % i)

content = open('C:\\test\\b.txt')
print(content.read())

#6
import string
alphabet= string.ascii_lowercase
for l in alphabet:
    open("C:\\test\\test2\\"+l+".txt",'w')

#7
with open('C:\\test\\a.txt', 'r') as fr, open('C:\\test\\b.txt', 'a') as se:
    for i in fr:
        se.write(i)

#8
if (os.path.isfile(f'C:\\test\\c.txt') == False):
    print("File does not exist")
else:
    print('Readable:', os.access('C:\\test\\c.txt', os.R_OK))
    print('Writable:', os.access('C:\\test\\c.txt', os.W_OK))
    print('Executable:', os.access('C:\\test\\c.txt', os.X_OK))
    os.remove("C:\\test\\c.txt")
