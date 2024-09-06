import random

# 고객 정보 노드
class Customer:
    def __init__(customerlist, name):
        customerlist.name = name
        customerlist.account_number = customerlist.generate_account_number()
        customerlist.balance = 0  # 초기 잔고는 0원

    # 10자리 계좌번호 난수 생성
    def generate_account_number(customerlist):
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])

    # 고객 정보 출력
    def display_info(customerlist):
        print(f"이름: {customerlist.name}, 계좌번호: {customerlist.account_number}, 잔고: {customerlist.balance}원")

# 고객 관리 시스템
class CustomerManagementSystem:
    def __init__(customerlist):
        customerlist.customers = []  # 고객 리스트

    # 고객 생성 (Create)
    def create_customer(customerlist, name):
        new_customer = Customer(name)
        customerlist.customers.append(new_customer)
        print(f"고객 '{name}'의 정보가 생성되었습니다.")
        new_customer.display_info()

    # 고객 삭제 (Delete)
    def delete_customer(customerlist, name):
        for customer in customerlist.customers:
            if customer.name == name:
                customerlist.customers.remove(customer)
                print(f"고객 '{name}'의 정보가 삭제되었습니다.")
                return
        print(f"'{name}' 고객을 찾을 수 없습니다.")

    # 고객 정보 수정 (Update)
    def update_customer(customerlist, name, new_name=None, deposit=None, withdraw=None):
        for customer in customerlist.customers:
            if customer.name == name:
                if new_name:
                    customer.name = new_name
                    print(f"이름이 '{new_name}'(으)로 변경되었습니다.")
                if deposit:
                    customer.balance += deposit
                    print(f"{deposit}원이 입금되었습니다. 현재 잔고: {customer.balance}원")
                if withdraw:
                    if withdraw <= customer.balance:
                        customer.balance -= withdraw
                        print(f"{withdraw}원이 출금되었습니다. 현재 잔고: {customer.balance}원")
                    else:
                        print("출금 금액이 잔고보다 큽니다.")
                return
        print(f"'{name}' 고객을 찾을 수 없습니다.")

    # 고객 검색 (Search)
    def search_customer(customerlist, name):
        for customer in customerlist.customers:
            if customer.name == name:
                print(f"'{name}' 고객의 정보:")
                customer.display_info()
                return
        print(f"'{name}' 고객을 찾을 수 없습니다.")

    # 전체 고객 목록 출력
    def display_all_customers(customerlist):
        if not customerlist.customers:
            print("등록된 고객이 없습니다.")
        else:
            for customer in customerlist.customers:
                customer.display_info()

# 사용자 입력을 받아 기능 실행
def main_menu():
    cms = CustomerManagementSystem()

    while True:
        print("\n원하시는 기능을 선택하세요:")
        print("1: Create (고객 생성)")
        print("2: Delete (고객 삭제)")
        print("3: Update (고객 정보 수정)")
        print("4: Search (고객 검색)")
        print("5: Exit (종료)")
        
        choice = input("번호를 입력하세요: ")

        if choice == "1":  # 고객 생성
            name = input("고객의 이름을 입력하세요: ")
            cms.create_customer(name)
        elif choice == "2":  # 고객 삭제
            name = input("삭제할 고객의 이름을 입력하세요: ")
            cms.delete_customer(name)
        elif choice == "3":  # 고객 정보 수정
            name = input("수정할 고객의 이름을 입력하세요: ")
            new_name = input("새 이름 (변경하지 않으려면 Enter): ") or None
            deposit = input("입금할 금액 (변경하지 않으려면 Enter): ")
            deposit = int(deposit) if deposit else None
            withdraw = input("출금할 금액 (변경하지 않으려면 Enter): ")
            withdraw = int(withdraw) if withdraw else None
            cms.update_customer(name, new_name=new_name, deposit=deposit, withdraw=withdraw)
        elif choice == "4":  # 고객 검색
            name = input("검색할 고객의 이름을 입력하세요: ")
            cms.search_customer(name)
        elif choice == "5":  # 프로그램 종료
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")

# 프로그램 실행
if __name__ == "__main__":
    main_menu()
