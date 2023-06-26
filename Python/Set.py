# 집합(set) - 중복 X, 순서 X

my_set = {1, 2, 2, 3, 3}
print(my_set)

javaDev = {"유재석", "김태호", "양세형"}
pythonDev = set({"유재석", "박명수"})

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(javaDev & pythonDev)
print(javaDev.intersection(pythonDev))

# 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
print(javaDev | pythonDev)
print(javaDev.union(pythonDev))   # 순서는 보장되지 않음

# 차집합 (java는 할 수 있지만 python은 할 수 없는 개발자)
print(javaDev - pythonDev)
print(javaDev.difference(pythonDev))

# 집합 원소의 수 증가 (python을 할 수 있는 개발자의 수가 늘어남)
pythonDev.add("김태호")
print(pythonDev)

# 집합 원소의 수 삭제 (java를 할 수 있는 개발자의 수가 줄어듦)
javaDev.remove("양세형")
print(javaDev)