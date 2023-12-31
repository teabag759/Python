# "w" : write
score_file = open("./Python/FileIO/score.txt", "w", encoding="utf8")
print("수학: 0", file=score_file)
print("영어: 50", file=score_file)
score_file.close()

# "a" : append
score_file = open("./Python/FileIO/score.txt", "a", encoding="utf8")
score_file.write("과학: 80")
score_file.write("\n코딩: 100")
score_file.close()

# "r" : read
score_file = open("./Python/FileIO/score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

# readline 
score_file = open("./Python/FileIO/score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="") # 줄별로 읽고 싶지 않으면 end=""로 처리 
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

# 파일의 총 line 수를 모를 때 -> 반복문 활용
score_file = open("./Python/FileIO/score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

# list의 형태로 저장
score_file = open("./Python/FileIO/score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # list의 형태로 저장 
for line in lines:
    print(line, end="")
score_file.close()


# pickle : 파이썬의 객체 자체를 파일로 저장 
import pickle
profile_file = open("./Python/FileIO/profile.pickle", "wb") # b : binary, pickle을 쓰기 위해선 항상 설정
profile = {"이름":"박명수", "나이": 30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("./Python/FileIO/profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기 
print(profile)
profile_file.close()


# with : 블럭을 벗어나면 자동으로 파일을 닫아줌 
with open("./Python/FileIO/profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("./Python/FileIO/study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("./Python/FileIO/study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())