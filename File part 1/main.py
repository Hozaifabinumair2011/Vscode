file = open('main.txt','r')
print(file.read())
file.close()


file = open('main.txt','r')
print(file.read(8))
file.close()

file = open('main.txt','a')
print(file.write("Hi my name is hozaifa"))
file.close()

file = open('main.txt','r')
print(file.readline())
file.close()

file = open('main.txt','r')
print(file.readlines())
file.close()

file = open('main.txt','r')
for i in file:
    print(i)
file.close()