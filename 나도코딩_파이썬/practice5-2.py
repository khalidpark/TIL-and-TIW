#######튜플 
# 변경되지않는 목록을 사용할때 , 속도가 빠르기때문

menu = ("돈까스", "치즈까스") #메뉴가 딱 고정일때
print(menu[0])
print(menu[1])

#menu.add("생선까스") #오류발생, 추가할수없기때문

name = "김종국"
age = 20
hobby = "코딩"
print (name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

########### 세트
# 집합 (set)
# 중복이 안되고, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "조세호"}
python = set(["유재석","박명수"])

#교집합 (java 와 python)
print(java & python)
print(java.intersection(python))

#합집합 (java 와 python 할수있는 개발자)
print(java | python)
print(java.union(python))

#차집합 (java는할줄알지만 python은 할줄모르는 개발자)
print(java-python)
print(java.difference(python))

#python 할잘아는사람 늘어났을때
python.add("김태호")
print(python)

#java를 까먹었을떄
java.remove("양세형")
print(java)