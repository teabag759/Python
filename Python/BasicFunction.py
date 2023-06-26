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



# 문자열 처리 함수 
python = "Python is Amazing"
print(python.lower())   # 모두 소문자로 
print(python.upper())   # 모두 대문자로 
print(python[0].isupper())  # 인덱스의 값이 대문자인지 확인(불리언)
print(len(python))  # 문자열의 길이를 반환
print(python.replace("Python", "Java")) # 해당되는 문자열을 새로운 단어로 변경 

index = python.index("n")   # 해당되는 문자의 인덱스를 알려줌 (해당 값이 첫번째로 나타나는 인덱스를 알려줌)
print(index)
index = python.index("n", index + 1)    # 해당되는 문자의 다음(두번째로 나타나는) 인덱스를 알려줌
print(index)

print(python.find("Java")) # 해당 단어가 문자열에 있는지 확인해줌 (없을 경우 "-1" 반환)
print(python.index("Java")) # 해당 단어가 문자열에 있는지 확인해줌 (없을 경우 오류가 나타남)

print(python.count("n"))  # 해당 문자가 문자열에 몇 번 있는지 알려줌 