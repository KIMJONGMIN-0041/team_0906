import random

class Customer :
    def __init__(self, name, money, address) :
        self.name = input("이름이 무엇인가요?")
        self.address = random.randrange(10000000, 99999999)
        self.money = 0