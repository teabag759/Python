def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):    # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):   # 출금
    if balance >= money :
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
    return balance - money

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission     # 튜플 형식으로 반환


balance = 500   # 잔액
balance = deposit(balance, 1000)
print(balance)

balance = withdraw(balance, 1000)
print(balance)

commission, balance = withdraw_night(balance, 400) 
print("수수료는 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))


#############################################################
# 기본값 설정 
def profile(name, age, main_lang):
    print("이름: {0} \t나이: {1} \t주 사용 언어: {2}".format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 30, "자바")

# 같은 학교, 같은 학년, 같은 반, 같은 수업 
def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0} \t나이: {1} \t주 사용 언어: {2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")


#############################################################
# 키워드 값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(age=32, name="김태호", main_lang="자바")


#############################################################
# 가변인자 
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0} \t나이: {1} \t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름: {0} \t나이: {1} \t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")


#############################################################
# 지역변수와 전역변수
# 지역변수 : 함수 내에서만 사용되는 것(함수 호출이 끝나면 사라짐)
# 전역변수 : 프로그램 내 어디서든 사용 가능한 변수 

bread = 10 

def delivery(persons):   
    # bread = 20  # 지역 변수로 함수 내에서만 쓰임
    global bread    # 전역 변수로 함수 외에서도 쓰임 
    bread = bread - persons
    print("(함수 내) 남은 빵: {0}".format(bread))

def delivery_return(bread, persons):
    bread = bread - persons
    print("(함수 내) 남은 빵: {0}".format(bread))
    return bread    # 함수 내에서 계산한 bread의 값을 외부로 전달 

print("전체 빵: {0}".format(bread))
delivery(2) 
bread = delivery_return(bread, 2)   # "bread = 10"의 값을 인수로 받음
print("남은 빵: {0}".format(bread))