year = int(input("연도를 입력하세요"))# 확인할 연도를 입력 받습니다.

leap_year = False   # 윤년인지 아닌지 체크할 변수로 기본 평년으로 체크
if year % 4 == 0:               # 4로 나누어떨어지는지 확인
    if year % 100 == 0:         # 100으로 나누어떨어지는지 확인
        if year % 400 == 0:     # 400으로 나누어떨어지는지 확인
            leap_year = True    # 4, 100, 400으로 나누어떨어지면 윤년
    else:
        leap_year = True # 4로 나누어떨어지고, 100으로 나누어떨어지지 않으면 윤년

if leap_year:
    print(year, "년은 윤년입니다.")
else:
    print(year, "년은 윤년이 아닙니다.")