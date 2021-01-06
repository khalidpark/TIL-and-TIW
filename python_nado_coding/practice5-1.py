#######리스트
#지하철 칸별로 10명, 20명, 30명
subway = [10, 20, 30]
print(subway)
subway = ["유재석","조세호","박명수"]
print(subway)

#조세호씨가 몇번째 칸에 타고 있는가?
print(subway.index("조세호")) #1, 1번째에 있다

#하하가 다음 정류장에서 탑승
subway.append("하하")
print(subway)

#정형돈씨를 유재석 / 조세호 사이에 탑승
subway.insert(1, "정형돈") #1번째에 집어넣어라 , 정형돈을
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

#같은 이름의 사람이 몇명 있는지 확인하기
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,34,2,1]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

#모두지우고싶어
num_list.clear()
print(num_list)

#다양한 자료형과 함께 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)

#리스트의 확장
num_list = [5,2,34,2,1]
num_list.extend(mix_list)
print(num_list)

#######사전
cabinet = {3:"유재석", 100:"김태호"} 
#3이라는 키는 유재석 , 100이라는 키는 김태호
print(cabinet[3])
print(cabinet[100])
#print(cabinet[5]) #오류발생후 프로그램 중단
print(cabinet.get(5)) #none값 출력후 다음 코딩 이어서 진행
print(cabinet.get(5, "사용가능")) #값이있으면 가져오고, 없으면 none 대체가능
print(3 in cabinet) #3이라는 키가 cabinet에 있느냐? #True, False

cabinet = {"A-3":"유재석", "B-100":"박명수"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새손님
print(cabinet)
cabinet["A-3"] = "김종국" #업데이트 가능
cabinet["C-20"] = "조세호" #추가

#간손님
del cabinet["A-3"]

#key 들만 출력
print(cabinet.keys())

#value들만 출력하려면
print(cabinet.values())

#key,value 쌍으로 출력
print(cabinet.items())

#폐점으로 삭제 전부
cabinet.clear()
print(cabinet)
