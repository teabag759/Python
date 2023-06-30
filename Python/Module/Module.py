# import theater_module
# theater_module.price(3) # 3명이서 영화보러 갔을 때 가격 
# theater_module.price_morning(4) # 4명이서 조조 영화보러 갔을 때 가격 
# theater_module.price_student(4) # 4명이서 영화보러 갔을 때 학생 할인 가격 

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_student(4)

# from theater_module import *    # 해당 모듈의 모든 것을 사용함을 선언
# price(3)
# price_morning(4)
# price_student(4)

# from theater_module import price, price_morning    # 해당 모듈에서 필요한 함수만 사용
# price(3)
# price_morning(4)
# # price_student(4)  # 오류 발생

from theater_module import price_student as student   # 해당 모듈에서 필요한 함수만 사용
student(5)
