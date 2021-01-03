#######메소드

#일반유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성되었습니다".format(self.name))
        print("체력{0}, 공격력{1}".format(self.hp, self.damage))

#공격유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다.[공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다".format(self.name, self.damage))
        self.hp -= damage
        print("{0} ; 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

#파이어뱃, 공격유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시") #self는 따로 보낼필요없기때문에 , location 정보만 보내주면 됨

#공격 2번 받았다고 가정하면
firebat1.damaged(25)
firebat1.damaged(25)

####### 상속

class Unit: #부모클래스
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit): #자식클래스
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage


####### 다중 상속
#부모가 2이상, 여러곳에서 상속받는경우

# 드랍쉽 : 공중유닛, 수송기, 공격기능 0

# 날수있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

#공중공격유닛클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리, 공중공격유닛, 한번에 14발 미사일발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")