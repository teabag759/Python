# 퀴즈 05
from random import *

boarding = 0

for customers in range(1, 51):
    time = randint(5, 51)
    if 5 <= time and time <= 15:
        print("[0] {0}번째 손님 (소요시간: {1})".format(customers, time))
        boarding += 1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1})".format(customers, time))

print("총 탑승 승객: {0}명".format(boarding))