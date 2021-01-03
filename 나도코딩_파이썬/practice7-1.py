####### 함수

def open_account():
    print("새로운 계좌가 생성되었습니다.")

#호출해도 아무것도 진행안됨, 함수는 정의만 한거고 따로 실행값을 세팅해줘야함

open_account()

####### 전달값과 반환값

def deposit(balance, money):
    print("입금이 온료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance + money 

def withdraw(balance, money):
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 온료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다".format(balacnce))
        return balance

def withdraw_night(balance, money):
    commission = 100 #출금수수료
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
#balance = withdraw(balance, 2000)
#balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance,500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission,balance))