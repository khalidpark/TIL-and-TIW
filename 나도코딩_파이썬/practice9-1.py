####### 클래스 ,어렵지만 꼭 필요한 내용

#마린 : 공격유닛, 군인, 총

name = "마린"
hp = 40
damage = 5

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력{0}, 공격력 {1} \n".format(hp, damage))

#탱크 : 공격유닛, 탱크 , 포 , 일반모드 / 시즈모드

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력{0}, 공격력 {1} \n".format(tank_hp, tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

#탱크가 늘어날수록 1,2,3,4 할수없다, 그래서 클래스가 필요하다, 클래스는 붕어빵기계로 비유된다
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성되었습니다".format(self.name))
        print("체력{0}, 공격력{1}".format(self.hp, self.damage))
       
marine1 = Unit("마린", 40, 5) #셀프 제외하고
marine2 = Unit("마린", 40, 5) #셀프 제외하고
tank = Unit("탱크", 150, 35)  #셀프 제외하고

####### __init__ 
#클래스로부터 생성되는 객체(마린,탱크)

#marine3 = Unit("마린") #오류발생,

####### 멤버변수
#self.name , self.hp, self.damage 에서 셀프 뒷 부분이 멤버변수

#레이스 : 공중유닛, 비행기, 클로킹 기능
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름은 {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True #클로킹 외부변수 할당해도 기존에 적용

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다".format(wraith2.name))

#if wraith1.clocking == True:
#   print("{0} 는 현재 클로킹 상태입니다".format(wraith2.name))
#오류발생, wraith1은 클로킹 변수 지정해주지 않았기 때문