# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호는 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈을 유재석/조세호 사이에 태우기 
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄 
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인하기
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬하기 
num_list = [5, 4, 3, 2, 1]
num_list.sort()    # 오름차순으로 정렬 
print(num_list)

num_list.reverse()  # 내림차순으로 정렬
print(num_list)

# 리스트 안 value 모두 지우기 
num_list.clear()
print(num_list)

# 다양한 자료형과 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트의 확장 
num_list.extend(mix_list)
print(num_list)