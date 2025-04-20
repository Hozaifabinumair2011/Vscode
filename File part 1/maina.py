file1 = open('main.txt','r')
file2 = open('maina.txt','w')
for i in file1.readlines():
    if (i.startswith('if')):
        print(i)
        file2.write(i)
file2.close()
file1.close()