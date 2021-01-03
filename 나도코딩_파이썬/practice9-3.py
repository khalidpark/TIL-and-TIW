####### 연산자 오버로딩

# 부모클래스 말고 자식 클래스에서 정의한 메소드를 쓰고싶을때, 메소드를 새롭게 정의해서 사용할때

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 스피드는 0으로 처리
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

#벌쳐 : 지상유닛, 기동성 좋음, 
vulture = AttackUnit("벌쳐", 80, 10, 20)

#배틀크루저 : 공중유닛, 체력좋고, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")

#지상은 move를 쓰고, 공중은 fly 쓰면 너무 귀찮으니까
#똑같이 move를 쓰면 지상은 이동하고, 공중은 날아가게 하자

vulture.move("11시")
#battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")


####### PASS

#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass #말그대로 그냥 넘어가기

#서플라이 디폿 : 건물 1개당 8만큼의 유닛 생산 가능
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

###### SUPER

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) #윗줄 아랫줄 동일뜻 , super쓸때는 self 없이
        self.location = location
