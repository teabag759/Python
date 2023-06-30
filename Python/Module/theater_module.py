# 모듈 : 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일

# 영화관
# 일반 가격 
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people * 10000))

# 조조 할인 
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))

# 학생 할인 
def price_student(people):
    print("{0}명 학생 할인 가격은 {1}원 입니다.".format(people, people * 5000))

    