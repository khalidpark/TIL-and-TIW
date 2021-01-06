####### continue와 break
absent = [2,5] #결석
no_book = [7] #책을 깜빡했음
for student in range(1,11): #1,2,3,4,5,6,7,8,9,10
    if student in absent : 
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0},책을 읽어봐".format(student))

####### 한 줄 for

#출석번호 1,2,3,4 앞에 100을 붙이기로 함 -> 101 102 103 104
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

#학생들 이름을 길이로 변환
students=["Iron man", "Thor", "I am Groot"]
students = [len(i) for i in students]
print(students)

#학생이름을 대문자로 변환
students=["Iron man", "Thor", "I am Groot"]
students = [i.upper() for i in students]
print(students)

####### 퀴즈5
#당신은 택시기사님
#50명의 승객과 매칭기회가 있을때, 총 탑승 승객 수를 구하는 프로그램
#조건1: 승객별 소요 시간은 5분 ~ 50분 난수
#조건2: 당신은 소용시간 5분 ~ 15분 사이의 승객만 매칭

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 3분)
# ...
# [] 50번째 손님 (소요시간 : 16분)
# 총 탑승 승객 : 2분

from random import *
cnt = 0 #총 탑승 승객 수
for i in range(1,51) : # 1~50 이라는 수 (승객)
    time = randrange(5,51) #5분에서 50분 소요시간
    if 5<=time<=15: #5~15분 이내 손님, 탐승 승객 수 증가 처리
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        cnt +=1
    else : #매칭실패한경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))

print("총 탑승 승객 : {0}분".format(cnt))