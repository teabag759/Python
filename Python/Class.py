# Class : 붕어빵 틀, 서로 연관있는 변수와 함수의 집합
# 스타크래프트로 예시 들기 

# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
name = "마린"   # 유닛의 이름
hp = 40     # 유닛의 체력
damage = 5  # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있음 (일반모드 / 시즈모드)
tank_name = "탱크"
tank_hp = 150     
tank_damage = 35  

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))


# 공격력 함수 
def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)



# 일반 유닛
class Unit :
    def __init__(self, name, hp):
        self.name = name    # 멤버변수 : class 내에서 정의된 변수 
        self.hp = hp 
        # self.damage = damage 
        # print("{0} 유닛이 생성되었습니다.".format(self.name))
        # print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)   
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
    # 하나의 클래스를 통해 서로 다른 유닛을 생성할 수 있음
    # 메서드 : 클래스 안에서 구현하는 함수 
        # 메서드의 첫번째 매개변수 이름은 인스턴스 자신 -> 관례적으로 self라는 이름을 사용 
    # __init__ : Python의 생성자, 객체가 생성되면 자동으로 호출되어 객체를 초기화 
    # 객체 : 어떤 클래스로부터 만들어지는 것 -> marine1, marine2, tank
    # 인스턴스 : 클래스의 객체가 소프트웨어에 실체화된 것 -> marine1, marine2, tank는 Unit class의 인스턴스! 
        # (instance는 특정 object가 어떤 class의 object인지 관계를 중점으로 표현할 때 사용)

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않는 기술)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) 
    # wraith1 뒤의 .을 통해 Unit의 멤버변수에 접근할 수 있음

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True     # Unit에 없는 외부 변수를 만들어 추가로 사용할 수 있음(확장한 객체에 대해서만 사용 가능)

if wraith2.clocking == True :
    print("{0}은(는) 현재 클로킹 상태입니다.".format(wraith2.name))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        # self.name = name    
        # self.hp = hp 
        Unit.__init__(self, name, hp)   # Unit(부모class)에서 상속받음 -> AttackUnit : 자식class
        self.damage = damage 
        # 메딕 : 체력을 회복시켜줌 (공격력이 없음) -> 일반 유닛에서 damage 변수가 필요 없음 
            # -> 일반 유닛에서 damage 변수 삭제, 공격 유닛인 경우에만 damage 변수 사용할 수 있도록 바꾸기 
            # => Unit에서 겹치는 내용을 AttackUnit에 상속!

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
            # self. ~ : 자기 자신의 변수에 접근, class 자기 자신의 멤버 변수의 값을 전달받음 
            # self가 없는 멤버변수 : 각 메소드에서 전달받은 값을 사용 
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 잆었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 파이어뱃 : 공격 유닛, 화염방사기 
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격을 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)


# 드랍쉽 : 공격 유닛, 수송기, 마린/파이어뱃/탱크 등을 수송, 공격 X
# 날 수 있는 기능을 가진 클래스 
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location) :
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


# 다중 상속 : 둘 이상의 부모 class에서 상속받는 것 
# 공중 공격 유닛 클래스 
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사 
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")



# 건물 생성
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # pass    # pass : 내부 구현 없더라도 따로 에러를 발생시키지 않고, 함수나 클래스 선언 가능 
        super().__init__(name, hp, 0)
            # super : 부모 클래스의 __init__() 매직 메소드를 자식 클래스의 __init__() 매직 메소드에서 실행
            # 다중 상속 시 super : 맨 처음에 상속받는 class의 생성자가 호출됨 
                # class BuildingUnit(Unit, Flyable):
                    # def __init__(self):
                        # super.__init__()  -> Unit 생성자가 호출됨 
                        # 다중 상속시 여러 생성자가 필요한 경우에는 super() 대신 각 class의 생성자를 호출하는 것이 좋음
            # 매직 메소드(특별 메소드) : __로 시작해서 __로 끝나는 메서드
        self.location = location 

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛 생성
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()