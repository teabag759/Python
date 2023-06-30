# 패키지 : 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일들의 폴더 형식

# import travel_Package.thailand
# import travel_Package.thailand.ThailandPackage # import 사용시 (thailand) 부분은 모듈이나 패키지만 가능
# trip_to = travel_Package.thailand.ThailandPackage()
# trip_to.detail()

# from travel_Package.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# import travel_Package.vietnam
# trip_to = travel_Package.vietnam.VietnamPackage()
# trip_to.detail()

# from travel_Package import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel_Package import *  # 오류 -> * travel_Package 의 공개 범위를 설정해주지 않음 -> __init__.py에서 설정
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()


# 패키지, 모듈 위치 확인 
import inspect  # 패키지, 모듈의 위치를 확인시켜줌
import random
print(inspect.getfile(random))
print(inspect.getfile(vietnam))