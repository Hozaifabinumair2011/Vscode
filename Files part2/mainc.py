a=open('document.txt','r')
data=a.read()
b=open('sample.txt','r')
data2=b.read()
datac=data+"\n"
datac=data+data2
file=open('merge.txt','w')
file.write(datac)