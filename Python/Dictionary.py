# 딕셔너리 {key : value}

cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) # print(cabinet[3]) 과 같은 결과 

# print(cabinet[5])   # 오류가 난 후 프로그램이 종료됨 ("Hi" 가 출력되지 않음)
print(cabinet.get(5))  # None이 출력됨 ("Hi" 가 출력됨)
print("Hi")

print(cabinet.get(5, "available"))  # 5 라는 key가 없을 경우 "available" 출력

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3" : "유재석", "B-100" : "김태호"}    # key는 string도 가능
print(cabinet["A-3"])
print(cabinet["B-100"])

# new value and update
print(cabinet)
cabinet["C-2"] = "조세호"
cabinet["A-3"] = "김종국"
print(cabinet)

# del
del cabinet["A-3"] 
print(cabinet)

# key들만 출력 
print(cabinet.keys())

# value들만 출력 
print(cabinet.values())

# key, value 쌍으로 출력 
print(cabinet.items())

# key와 value 모두 삭제 
print(cabinet.clear())
