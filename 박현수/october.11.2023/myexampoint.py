print("공개하시긴 마음에 큰 불편함과 슬픔이 공존하겠지만 당신의 시험 점수를 공개 하여 주실 수 있습니까?")

point = int(input("당신의 시험점수를 입력하여주세요: "))

if point >= 90:
    print("와우, 당신의 점수는 %d 이기 때문에 당신의 성적은 A 입니다. 부럽네요." %point)
elif point >= 80:
    print("당신의 점수는 %d 이기 때문에 당신의 성적은 B 입니다. 무난하네요." %point)
elif point >= 70:
    print("당신의 점수는 %d 이기 때문에 당신의 성적은 C 입니다. 좀 열심히 하지 그랬어요." %point)
elif point >= 60:
    print("당신의 점수는 %d 이기 때문에 당신의 성적은 D 입니다. 엄마한테 등짝스메싱 맞겠네요." %point)
else:
    print("당신의 점수가 바닥을 기고 있네요. %d점이라니, 무려 F입니다. 공부좀 합시다." %point)