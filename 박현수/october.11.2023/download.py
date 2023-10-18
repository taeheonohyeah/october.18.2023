yesorno = int(input("다운로드 받으시겠습니까? 그렇다면 0을 누르십시오"))

percent = 10000

while True:
    print("다운로드 받는 중... %d 퍼센트 남음" %(percent/100))
    percent = percent - 1

    if percent == 0:
        break