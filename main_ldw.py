from Account_ldw import Account # Account 모듈 가져오기
from Deposit import deposit
account = [] # 계좌 저장 공간으로 계좌가 생성될 때마다 
while True :
    num = int(input("1 : 생성\n2 : 입금\n3 : 출금\n4 : 송금\n5 : 계좌정보조회\n나머지 번호: 종료"))
    if num == 1 : # 계좌 생성
        account.append(Account())

    elif num == 2 : # 이름을 먼저 묻고 account 리스트에서 계좌를 찾은 다음 돈을 입력받아 입금시킨다.
        name = input("이름이 무엇인가요?")
        for i in range(len(account)) :
            if(account[i].name == name) :
                deposit(account[i])
                break;
    
    elif num == 3 : # 이름을 먼저 묻고 account 리스트에서 계좌를 찾은 다음 돈을 입력받아 출금시킨다. 만약에 계좌에 돈이 없으면 돈이 없다고 출력된다.
        name = input("이름이 무엇인가요?")
        for i in range(len(account)) :
            if(account[i].name == name) :
                account[i].withdraw()
                break;
            if(i == len(account) - 1) :
                print("이름이 없습니다.")

    elif num == 4 : # 이름을 먼저 묻고 account 리스트에서 계좌를 찾은 다음 돈과 계좌이름을 입력받아 돈을 송금시킨다. 만약에 계좌에 돈이 없으면 돈이 없다고 출력된다.
        name = input("이름이 무엇인가요?")
        for i in range(len(account)) :
            if(account[i].name == name) :
                myname = account[i]
                otherName = input("보내실 분의 이름을 적어주세요")
                money = int(input("얼마를 보내실건가요?"))
                flag = 1
                for j in range(len(account)) :
                    if(account[j].name == otherName) :
                        myname.send(account[j])
                        flag = 0
                        break
                if(flag == 0) :
                    break
            if(i == len(account) - 1) :
                print("이름이 없습니다.")
    elif num == 5 : # 계좌 정보를 출력한다.
        name = input("이름이 무엇인가요?")
        for i in range(len(account)) :
            if(account[i].name == name) :
                account[i].accountinformation()
    else : 
        print("종료되었습니다.")
        break;
        
                
