# 퀴즈 08
class House: 
    # 매물 초기화 
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year


    # 매물 정보 표시 
    def show_detail(self):
        print("위치: {0}".format(self.location))
        print("주거유형: {0}".format(self.house_type))
        print("거래유형: {0}".format(self.deal_type))
        print("가격: {0}".format(self.price))
        print("완공연도: {0}".format(self.completion_year))
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)


houses = []
house1 = House("강남", "아파트", "매매", "10억", "2013년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()
    print()


