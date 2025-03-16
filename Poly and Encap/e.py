class computer:
    def __init__(self):
        self.__price=900
    def sell(self):
        print(self.__price)
    def max(self,p):
        self.__price=p
c=computer()
c.sell()
c.__price=1000
c.sell()
c.max(1000)
c.sell()