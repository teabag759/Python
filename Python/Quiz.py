# 퀴즈 03
prevPassword = "http://naver.com"
sitePassword = prevPassword[7:-4]

createPassword = sitePassword[:3] + str(len(sitePassword)) + str(sitePassword.count("e")) + "!"

print(createPassword)

########### 다른 풀이법 ###########
# url = "http://naver.com"
# url = "http://daum.net"
url = "http://google.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]     # my_str[0:5]
password = my_str[:3] + str(len(my_str)) +str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))



##################################
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
