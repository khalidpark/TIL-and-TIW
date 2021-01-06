#######숫자자료형

print(5)
print(-10)
print(3.14)
print(1000000)
print(5+3)
print(3*2)
print(3*(3+2))

#######문자열 자료형

print('풍선')  #''작은따옴표
print("나비")  #""큰따옴표 (둘다상관없이 문자열 출력)
print("나비"*15)  #문자열과 숫자함께 출력가능

#######boolean 자료형 (참과 거짓)

print(5>10) #False
print(5<10) #True
print(True)
print(not True)
print(not (5>10))

name = "파이썬"
animal = "강아지"
age = 4 #숫자는 정수니까 그냥바로
hobby = "산책"
is_adult = age >= 3

print("우리집 강아지의 이름은 파이썬입니다")
print("파이썬은 4살이며, 산책을 아주 좋아해요")
print("파이썬은 어른일까요? True")

print("우리집 " + animal + "의 이름은 " + name + "입니다")
hobby = "공놀이" #위에 hobby 선언되어있지만 아래 다시 선언되면 아래쪽을 반영
print(name + "는 " + str(age) + "이며, " + hobby + "을 아주 좋아해요") #정수형은 'str'을 활용해서 문자열로 바꿔줘야함
print(name, "는 " ,age, "이며, " ,hobby, "을 아주 좋아해요") # +말고 ,도 가능, ,로할경우 str 필요없이 정수 바로반영가능
print(name + "는 어른일까요?" + str(is_adult)) #boolean형도 str로 감싸줘야한다

'''
이렇게 작은따옴표 3개 넣고
남기면 전부다
이 내용이 주석처리가 됩니다
'''

#문장 전체를 긁어놓고 '컨트롤 + 슬러쉬' 버튼누르면 됨

#######퀴즈1
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")