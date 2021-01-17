'''with open('file.txt', 'r') as f:
    print(f.read(5))
    print(f.read())
    print(f.tell())'''

with open('file.txt', 'r') as f:
    print(f.read(5))
    print(f.tell())
    f.seek(0, 1)
    print(f.read(10))
    print(f.tell())
    