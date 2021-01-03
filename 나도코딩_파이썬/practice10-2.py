####### 퀴즈9
#치킨집, 자동주문시스템 코드확인후 적절한 예외처리 구문 넣기

# 조건 1 :1보다 작거나 숫자가 아닌 값은 ValueError 처리
# 출력메시지 : 잘못된 값을 입력하였습니다

#조건2 : 대기 손님이 주문할수있는 총 치킨량 10마리
#치킨 소진시 사용자 정의에러(SoldOutError) 발생시키고 프로그램 종료
#출력메시지 : 재고 소진되어 더이상 주문 받지 않습니다

#코드
class SoldOutError(Exception):
    pass  

chicken = 10
waiting = 1 #홀 안에는 만석, 대기번호 1부터 시작
while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇마리 주문하시겠습니까?"))
        if order > chicken : #남은 치킨보다 주문량이 많을때
            print("재료가 부족합니다")
        elif order <=0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다".format(waiting,order))
            waiting += 1
            chicken -= order
        if chicken ==0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다")
    except SoldOutError:
        print("재고 소진되어 더이상 주문 받지 않습니다")
        break