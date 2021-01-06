####### 표준입출력

print("Python", "Java") #출력값 : Python Java
print("Python", "Java", sep=",") #출력값 : Python,Java
print("Python", "Java", sep=" vs ") #출력값 : Python vs Java
print("Python", "Java", "Java Script" ,sep=" vs ") #출력값 : Python vs Java vs Java Script

print("Python", "Java", sep=",", end="?") #end=문장의 끝부분은 ?로 바꿔주세요 #Python,Java?무엇이 더 재밌을까요?
print("무엇이 더 재밌을까요?")

#시험 성적
scores = {"수학":0 , "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject, score)
#수학 0
#영어 50
#코딩 100

scores = {"수학":0 , "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":") #left정렬, 8칸 확보 후 / right정렬 , 4개 크기 확보 후
#수학      :   0
#영어      :  50
#코딩      : 100

#은행에 갔을때 대기순번표
# 001, 002, 003, 004

for num in range(1,21):
    print("대기번호 :" + str(num))
#대기번호 :1
#대기번호 :2
#대기번호 :3
#대기번호 :4

for num in range(1,21):
    print("대기번호 :" + str(num).zfill(3)) #zfill 0을 채운다, 3크기만큼 공간 확보후 빈공간은 zero로 채워줘
#대기번호 :001
#대기번호 :002
#대기번호 :003
#대기번호 :004

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은" + answer + "입니다.")

#입력하신 값은 10 입니다
#입력하신 값은 나도코딩 입니다

#10 이라는 숫자 int 지만 출력이됨 str로 감싸주지 않아도 . 왜?
# input 으로 입력되어 들어가는 입력값은 무조건 문자열로 인식되어 들어감