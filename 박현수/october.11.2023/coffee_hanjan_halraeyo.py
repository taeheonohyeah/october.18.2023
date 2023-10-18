#커피머신
coffee = 10

while True: #while문을 쓰는 이유는 계속 반복ㄱ시키고 싶을 때 ~동안 ~동안 / if문은 만약에
    money = int(input("돈을 투입해주세요: "))

    if money == 5000: 
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 5000:
        print("입력하신 금액은 %d원, 거스름돈 %d원을 주고 커피를 줍니다." %(money, money-5000))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d입니다." %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중단합니다.")
        #break #break를 적은 이유는 무한반복문인 while True가 계속 수행되기 때문에
    #강제로 문을 빠져나간다 