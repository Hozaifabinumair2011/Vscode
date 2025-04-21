file=open('document.txt','r')
a=file.readlines()
for i in a:
    w=i.split()
    print(w)
file.close()