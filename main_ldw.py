import Account_ldw # Account 모듈 가져오기

account = []
while True :
    num = int(input("1 : 생성\n2 : 입금\n3 : 출금\n4 : 송금\n5 : 계좌정보조회\n나머지 번호: 제거"))
    if num == 1 : # 계좌 생성
        account.append(Account_ldw.Account())
    elif num == 2 :
        name = input("이름이 무엇인가요?")
        for i in range(len(account)) :
            if(account[i].name == name) :
                account[i].deposit()
                break;
    elif num == 3 :
        name = input("이름이 무엇인가요?")
        for i in range(len(account)) :
            if(account[i].name == name) :
                account[i].withdraw()
                break;
            if(i == len(account) - 1) :
                print("이름이 없습니다.")
    elif num == 4 :
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
    elif num == 5 :
        name = input("이름이 무엇인가요?")
        for i in range(len(account)) :
            if(account[i].name == name) :
                account[i].accountinformation()
        
                
