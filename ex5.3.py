f =  open ('file.txt', 'r')

data = f.read(1024)#1024 byth размер читаемых данных

'''content = f.readlines()
for line in content:
    print(line)'''

for line in f:
    print(line)

f.close()