
# 퀴즈 04

from random import *

id = []
for i in range(1, 21) :
    id.append(i)

shuffle(id)

chicken = set(sample(id, 1))
coffee = set(sample(id, 3))

duplication = chicken & coffee

print(" -- 당첨자 발표 -- ")
print(" 치킨 당첨자: " + str(chicken - (duplication))) # set로 출력 
print(" 커피 당첨자: " + str(coffee - (duplication)))
print(" -- 축하합니다! -- ")
    

########### 다른 풀이법 ###########
users = range(1, 21)    # type = range
users = list(users)

shuffle(users)

winners = sample(users, 4)  # 아예 네 명을 뽑아서 중복의 가능성을 차단..!

print(" -- 당첨자 발표 -- ")
print(" 치킨 당첨자: {0}".format(winners[0]))
print(" 치킨 당첨자: {0}".format(winners[1:]))
print(" -- 축하합니다! -- ")

