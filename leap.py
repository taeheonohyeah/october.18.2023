year = int(input("년도를 입력하세요"))

if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    print("%d년은 윤년입니다" %year)
else:
    print("%d년은 평년입니다" %year)