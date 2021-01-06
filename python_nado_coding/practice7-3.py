#######지역변수와 전역변수
#지역변수 : 함수내에서만 쓸수있는 변수
#변역변수 : 프로그램 어디서든 쓸수있는 변수

gun = 10

def checkpoint(soldiers): #경계근무
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print ("전체 총 : {0}".format(gun)) #전체 총 : 10
checkpoint(2) #2명이 경계 근무 하러 나감 #[함수 내] 남은 총 : 18
print ("남은 총 : {0}".format(gun)) #남은 총 : 10

gun = 10

def checkpoint(soldiers): 
    global gun #전역공간에 있는 (16줄에있는) gun 을쓰겠다
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print ("전체 총 : {0}".format(gun)) #전체 총 : 10
checkpoint(2) #2명이 경계 근무 하러 나감 #[함수 내] 남은 총 : 8
print ("남은 총 : {0}".format(gun)) #남은 총 : 8

def checkpoint_ret(gun, soldiers): 
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun
gun = checkpoint_ret(gun, 2)
print ("남은 총 : {0}".format(gun)) #남은 총 : 8


#######퀴즈6
#표준체중을 구하는 프로그램을 작성하시오
#표준체중 : 각 개인의 키에 적당한 체중

#남자 : 키(m) * 키(m) * 22
#여자 : 키(m) * 키(m) * 21

#조건 1 : 표준 체중은 별도의 함수 내에서 계산
#함수명 : Std_weight
#전달값 : 키(height), 성별(gender)
#조건2 : 표준 체중은 소수점 둘째자리까지 표시

#(출력예제)
#키 175cm 남자의 표준 체중은 67.38kg입니다.

def std_weight(height, gender): #키는 m단위(실수), 성별 "남자"/"여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 #cm 단위
gender = "남자"    
weight = round(std_weight(height / 100, gender), 2) #라운드함수 감싸고 소수점 '2'자리 까지만 표시해줘
print ("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))


