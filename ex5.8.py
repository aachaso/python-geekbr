'''with open('file.txt', 'a') as f:
    data = f.write('\n new')'''

with open('file_two.txt', 'r+') as f:
    data = f.write('\nnew')
    print(f.name)
    print(f.closed)
    print(f.mode)
