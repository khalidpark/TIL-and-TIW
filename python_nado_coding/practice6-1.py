#######if

#if 조건:
#    실행 명령문

weather = "비"
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

weather = input("오늘 날씨는 어때요?") #커서가 나오고 입력문을 기다리고있음
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")


weather = input("오늘 날씨는 어때요?") # 커서가 나오고 입력문을 기다리고있음
if weather == "비" or weather =="눈" : # or를 통해 조건추가가능 
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")


temp = int(input("기온은 어때요?")) #input값은 문자이기 때문에 int를 통해 숫자열로 변경해주기
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <=temp and temp <30:
    print("괜찮은 날씨예요")
elif 0<= temp <10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지마세요")

#######for 반복문

print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waiting_no in [0,1,2,3,4]:
    print("대기번호 :{0}".format(waiting_no))

for waiting_no in range(5): #0, 1, 2, 3, 4
    print("대기번호 :{0}".format(waiting_no))

for waiting_no in range(1, 6): #1, 2, 3, 4, 5
    print("대기번호 :{0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

####### while 반복문 / 어떤 조건이 만족할때까지 반복하라는 뜻

customer = "토르"
index = 5
while index >=1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요".format(customer,index))
    index -= 1
    if index ==0:
        print("커피는 폐기처분되었습니다")


customer = "아이언맨"
index = 1
while True: #무한루프, 계속진행할때
    print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer,index))
    index += 1
    #강제종료는 Ctrl + C

customer = "토르"
person = "unknown"

while person != customer : #해당 조건이 만족할때까지 계속 , person이 customer가 되면 종료
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")




number = 
time = 
    print("{0}번째 손님 (소요시간 : {1}분)".format(number,time))