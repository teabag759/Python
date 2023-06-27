import sys

print("Python", "Java", file=sys.stdout)    # 표준 출력
print("Python", "Java", file=sys.stderr)    # 표준 에러 스트림으로 전달되어 에러 메시지로 처리

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subjects, scores in scores.items() :
    # print(subjects, scores)
    print(subjects.ljust(4), str(scores).rjust(4), sep=":") # ljust() : 왼쪽 정렬 / rjust() : 오른쪽 정렬

# 은행 대기 순서표 뽑기 (예. 001, 002, ...)
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))    # zfill() : 값이 없는 빈 공간에는 '0'을 채움

answer = input("아무 값이나 입력하세요: ")  # input() : 입력받은 값의 type = str
print("입력하신 값은 " + answer + "입니다.")



######################################################
# 다양한 출력 포맷
# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되 총 10자리 공간 확보 
print("{0: > 10}".format(500))

# 부호 표시 : 양수일 땐 +, 음수일 땐 - 
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬, 빈칸으로 _ 로 채우기 
print("{0:_<10}".format(500))

# 3자리 마다 콤마 찍기 
print("{0:,}".format(1000000000000000000))

# 3자리 마다 콤마 찍기, +- 부호 표시
print("{0:+,}".format(1000000000000000000))
print("{0:+,}".format(-1000000000000000000))

# 3자리 마다 콤마 찍기, 부호 표시, 자릿수 확보, 빈자리는 ^로 채우기
print("{0:^<+30,}".format(1000000000000000000))

# 소수점 출력 
print("{0:f}".format(100000000000)) # 기본 6자리로 표시

# 소수점 특정 자리수까지 표시(소수점 셋째 자리에서 반올림)
print("{0:.2f}".format(5/3))