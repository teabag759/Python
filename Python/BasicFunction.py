print(abs(-5))  # 절대값, 5
print(pow(4, 2))    # 제곱값, 4**2 = 16
print(max(5, 12))   # 5~12 사이의 max, 12
print(min(5, 12))   # 5~12 사이의 min, 5
print(round(3.14))  # 반올림, 3
print(round(4.99))  # 반올림, 5


from math import *  # math library
print(floor(4.99))  # 내림, 4
print(ceil(3.14))   # 올림, 4
print(sqrt(16))     # 제곱근, 4


# 랜덤 함수 
from random import *
print(random())     # 0.0 이상 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 이상 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0.0 이상 ~ 10.0 미만의 임의의 정수 생성
print(int(random() * 10) + 1) # 1 이상 ~ 10 이하의 임의의 정수 생성

print(int(random() * 45) + 1) # 1 이상 ~ 45 이하의 임의의 정수 생성 
print(randrange(1, 46)) # 1 이상 ~ 46 미만의 임의의 정수 생성 
print(randint(1, 45))   # 1 이상 ~ 45 이하의 임의의 정수 생성 


# 퀴즈
print("오프라인 스터디 모임 날짜는 매월 " + str(randint(4, 28)) + "일로 선정되었습니다.")