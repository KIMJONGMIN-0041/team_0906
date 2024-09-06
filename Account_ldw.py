import random

class Account :
    def __init__(self) :  # 생성자로 모든 멤버변수를 초기화시킨다.
        self.name = input("이름이 무엇인가요?")
        self.address = random.randrange(1000000000, 9999999999) # 10자리수를 랜덤하게 받는다.
        self.money = 0
    
    def deposit(self) : 
        money = int(input("얼마를 입금하실건가요?")) 
        self.money += money

    def withdraw(self) :
        money = int(input("얼마를 출금하실건가요?"))
        if self.money >= money :
            self.money -= money
        else :
            print("출금할 돈이 모자랍니다.")
    
    def send(self, address) : # 다른 계좌(address)를 매개변수로 받아 송금시킨다.
        if self.money >= 0 :
            self.money -= address.money
            address.money += self.money
        else :
            print("돈이 없습니다.")
    
    def accountinformation(self) : # 계좌 정보를 출력한다.
        print("이름 : ", self.name)
        print("계좌번호 : ", self.address)
        print("잔고 : ", self.money)

            