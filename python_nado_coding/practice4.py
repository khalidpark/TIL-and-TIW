#######문자열

sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년, 
파이썬은 쉬워요 진짜
"""
print(sentence3) 

#######슬라이싱

jumin = "881138-1923754"
print("성별:" + jumin[7]) #8번째이나 코딩에서 시작은 0부터
print("연:" + jumin[0:2]) #0번째부터 2번째'미만'까지
print("월:"+jumin[2:4]) #2번째부터 4번째'미만'(직전)까지
print("생년월일:"+jumin[:6]) #시작이 처음부터면 0부터 표현안해도 됨
print("뒷7자리:"+jumin[7:]) #7번째부터 끝까지
print("뒷7자리 (뒤에서부터)"+jumin[-7:])
#제일뒤는-1, 제일뒤에서부터 7자리부터 싹 긁어오기

#######문자열 처리함수

python = "Python is Amazing"
print(python.lower()) #모두 소문자로 출력
print(python.upper()) #모두 대문자로 출력
print(python[0].isupper()) #0번째문자가 대문자면 트루
print(len(python)) #총 글자수
print(python.replace("Python","Java")) #찾아바꾸기

index = python.index("n") #n이라는 글자가 몇번째에 있는지
print(index) #5
index = python.index("n", index+1) #처음에 찾은거말고 그다음거부터 찾았을때
print(index)

print(python.find("Java")) #결과값 -1, find는 찾는게 없을때 -1 반환
#print(python.index("Java")) #에러, index는 찾는게 없을때 에러
print(python.count("n")) #'n'이 총 몇번들어가있는지 

#######문자열포맷

#방법1
print("나는 %d살입니다." %20) # %d 정수를 넣겠다
print("나는 %s를 좋아해요" %"파이썬") # %s 문자열을 넣겠다
print("Apple은 %c로 시작해요" % "A") # %c 는 캐릭터라서 한글자만 받겠다
print("나는 %s살입니다" %20) # %s 숫자도 가능하다
print("나는 %s색과 %s색을 좋아해요" %("파랑","빨강")) #두가지이상 넣고싶을때 

#방법2
print("나는 {}살입니다" .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파랑","빨강")) #두가지이상 넣고싶을때 
print("나는 {1}색과 {0}색을 좋아해요" .format("파랑","빨강")) #0번째문자열, 1번째문자열
#나는 빨강색과 파랑색을 좋아해요

#방법3
print("나는 {age}살이며 , {color}색을 좋아해요". format(age = 30, color = "파랑"))

#방법4 (version 3.6 이상~)
age = 20
color = "노랑"
print(f"나는 {age}살이며 , {color}색을 좋아해요") # 'f'로 시작하면 위에 지정한 값을 적용해서 보여줌

#######탈출문자
#/n : 문장내에서 줄바꿈해주세요
print("백문이 불여일견,/n 백견이 불여일타")

#\" \' 역슬래쉬 뒤 따옴표는 문장내에서 단순 따옴표 역할
# 저는 "나도코딩"입니다... 를 출력하고 싶을때

#print("나는 "나도코딩"입니다") #오류발생
print("나는 '나도코딩'입니다") #큰따옴표로 뽑아내고 싶은데
print('나는 "나도코딩"입니다') #작은따옴표로 시작 잘 안하는데
print("나는 \"나도코딩\"입니다")

# \\ 두번쓰면 문장 내에서는 하나의 \로 변경됨
print("c://Users//khalid//Desktop//pythonworkspace") #하나만 쓰면 경로표시불가 오류발생

# \r : 커서를 맨 앞으로 이동 후 덮어쓰기 #PineApple
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redb\bApple")

# \t : 탭
print("Red\tApple")

#######Quiz3

# naver = "http://naver.com"
# 규칙1 = naver[7:]
# print(규칙1)
# 규칙2 = 규칙1[0:5]
# print(규칙2)
# 규칙3 = 규칙2[:3] + len("규칙2") + 규칙2.count("e") + "!"
# print("규칙3")

#url = "http://naver.com"
url = "http://google.com"
my_str = url.replace("http://","") #규칙1
my_str = my_str[:my_str.index(".")] #규칙2
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}사이트의 비밀번호는 {1}입니다".format(url, password))