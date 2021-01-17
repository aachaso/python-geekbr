f = open ('file.txt', 'r')
'''content1 = f.readline()
content2 = f.readline()
content3 = f.readline()'''

content = f.readlines()
print(content)
f.close()