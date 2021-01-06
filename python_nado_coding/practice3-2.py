#######숫자처리함수

print(abs(-5)) #절대값 #5
print(pow(4,2)) #4^2 = 4*4 = 16
print(max(5,12)) #최대값을 찾아서 뽑아주는역할 , 12
print(min(5,12)) #최소값을 찾아서 뽑아주는역할 , 5
print(round(3.14)) #반올림,  3
print(round(4.99)) #반올림 , 5

from math import *
print(floor(4.99)) #내림 , 4
print(ceil(3.14)) #올림 , 4
print(sqrt(16)) #제곱근, 16의제곱근 , 4

#######랜덤함수

from random import *

print(random()) #랜덤함수를 통해 난수를 뽑음 , 0.0 ~ 1.0 '미만'의 임의값
print(random()*10) #0.0~10.0 미만의 임의 값 생성
print(int(random()*10)) #int 소수점뒤는 빼고
print(int(random()*10)+1) #1~10 이하의 임의의 값 생성
print(int(random()*45)+1) #1~45 이하의 임의의 값 생성
print(randrange(1,45)) #1~45 '미만'의 임의의 값 생성
print(randrange(1,46)) #1~46 '미만'의 임의의 값 생성
print(randint(1,45)) #1~45 '이하'의 임의의 값 생성

####### Quiz2
date =randint(4,28)
print(date)

print ("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다")
