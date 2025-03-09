class person(object):
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name)
        print(self.id)
class employe(person):
    def __init__(self,name,id,salary):
        self.salary=salary
        person.__init__(self,name,id)
a=employe("Eshan",70,100000000000000)
a.display()