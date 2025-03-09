from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class Human(animal):
    def move(self):
        print("I can walk and run")
class snake(animal):
    def move(self):
        print("I can crawl")
class dog(animal):
    def move(self):
        print("I can bark!")
a=Human()
a.move()
b=snake()
b.move()
c=dog()
c.move()