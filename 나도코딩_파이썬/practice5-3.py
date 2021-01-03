#######자료구조의 변경

menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

muenu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

#######Quiz4

#파이선코딩대회
#댓글이벤트 진행
#추첨통해 1명은 치킨, 3명은 커피
#추첨 프로그램 만드시오
#조건1: 편의상 댓글작성인원은 총 20명, 아이디는 1~20
#조건2: 댓글내용상관없이 추첨하되, 중복불가
#조건3: random모듈의 shuffle과 sample 활용

#출력예제
#---당첨자발표---
#치킨 당첨자 : 1
#커피 당첨자 : [2,3,4]
#---축하합니다---
from random import *
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#lst = range(1,21) #range함수, 1부터 21직전까지
print(type(lst)) #range type

shuffle(lst)

#한번에 4명을 뽑고나서 나눠야 중복을 피할수있다

winners = sample (lst,4) #4명중에서 한명은 치킨, 3명은 커피를 주면 됨

print("당첨자 발표")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("축하합니다")

