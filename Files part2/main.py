with open('document.txt','r') as file:
    data = file.readlines()
    for i in data:
        word=i.split()
        print(word)
file.close()

a=open('new.txt','x')
