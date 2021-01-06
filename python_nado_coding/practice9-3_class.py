class Unit:
    def __init__(self):
        print ("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable): #Flyable 생성자 즉 뒷 명령어는 생성안됨
    def __init__(self):
        super().__init__()

#드랍쉽
dropship = FlyableUnit()
#Unit 생성자

#########################################

class Unit:
    def __init__(self):
        print ("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit): #Unit 생성자 즉 뒷 명령어는 생성안됨
    def __init__(self):
        super().__init__()

#드랍쉽
dropship = FlyableUnit()
#Flyable 생성자

#########################################

#다중상속을할때는, 모든 부모 클래스 초기화가 필요할때는

class Unit:
    def __init__(self):
        print ("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit): 
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

#드랍쉽
dropship = FlyableUnit()
#Unit 생성자
#Flyable 생성자