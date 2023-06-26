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