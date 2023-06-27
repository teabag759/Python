# 퀴즈 06
def std_weight(height, gender):
    if gender == "여자":
        height_float = height / 100
        std_weight = height_float * height_float * 21
        print("키 {}cm {}의 표준 체중은 {:.2f}kg 입니다.".format(height, gender, std_weight))
    else:
        height_float = height / 100
        std_weight = height_float * height_float * 22
        print("키 {0}cm {1}의 표준 체중은 {2:.2f}kg 입니다.".format(height, gender, std_weight))
        
    return std_weight
    
std_weight(175, "여자")




####################################################
# 다른 풀이법 
def std_weight(height, gender): # 키 m단위(실수), 성별 "여자"/"남자"
    if gender == "여자":
        return height * height * 21
    else:
        return height * height * 22

height = 175 
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2:.2f}kg 입니다.".format(height, gender, weight))