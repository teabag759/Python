# 예외처리 : 프로그래머가 예기치못한 예외의 발생에 미리 대처하는 코드를 작성하는 것

# 사용자 정의 예외처리
class BigNumberError(Exception):
    # pass
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg



try:
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
    nums.append(int(input("두 번째 숫자를 입력하세요: ")))
    #nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")

except ZeroDivisionError as err: # as err : 발생하는 에러 문장을 출력
    print(err)

# nums.append(int(nums[0]/nums[1])) 문장을 작성하지 않은 경우
except Exception as err:    # Exception as err : 해당 에러 메시지를 받고 싶은 경우
    print("알 수 없는 오류가 발생하였습니다.")
    print(err)



# 의도적으로 에러 발생시키기
try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:    # 에러 발생
        # raise ValueError
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("한 자리 숫자만 입력하세요.")

# 사용자 정의 예외
except BigNumberError as err:
    print("잘못된 범위입니다. 한 자리 숫자만 입력하세요.")
    print(err)

# finally : 에러 발생 유무와 관계없이 무조건 실행이 되는 문장 
finally : 
    print("계산기를 이용해 주셔서 감사합니다.")

