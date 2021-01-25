class Car():
  wheel = 4
  doors = 4
  windows = 4
  seats = 4

# car는 클래스 (블루프린트 ,설계도)

porche = Car()
porche.color = "Red"

# porche는 instance


print(porche)
print(porche.color)

ferrari = Car()
ferrari.color = "Yellow"

print(ferrari)


def start():
  print("I started")
# 이거는 function

  def start():
    print("I started")
# 이거는 method (function에서 한칸 띈거)
# method 는 class 안에 있는 function

porche = Car()
porche.color = "Red and Super Red"
porche.start()

# 파이썬은 method를 호출할 때, 그 method의 instance를 첫번째 argument로 사용한다

#porche.start()
#즉
#porche.start(porche)


  def start(self):
    print(self.doors)
    print("I started")

porche = Car()
porche.start()
#=> 4
#=> I started