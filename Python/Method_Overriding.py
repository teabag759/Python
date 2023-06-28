# 메서드 오버라이딩 : 객체 지향 프로그래밍에서 자식 클래스가 자신의 부모 클래스들 중 
    # 하나에 의해 이미 제공된 메소드를 특정한 형태로 구현하는 것을 제공하는 언어의 특징


# 일반 유닛
class Unit :
    def __init__(self, name, hp, speed):
        self.name = name    
        self.hp = hp 
        self.speed = speed


    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))


# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)   
        self.damage = damage 


    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 잆었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 날 수 있는 기능을 가진 클래스 
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location) :
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed는 0으로 처리
        Flyable.__init__(self, flying_speed)

    # 메소드 오버라이딩을 통해 지상 유닛과 공중 유닛을 자동으로 확인할 수 있도록 함
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# # 벌쳐 : 지상 유닛, 기동성이 좋음 
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중 유닛, 체력과 공격력이 좋음 
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")    # 지상 유닛 -> 이동 
# # battlecruiser.fly(battlecruiser.name, "9시")    # 공중 유닛 -> 날아감
# battlecruiser.move("9시")

