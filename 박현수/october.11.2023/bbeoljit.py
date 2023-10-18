love = int(input("현수가 그녀를 사랑합니까? 1을 눌러 아니요, 0를 눌러 예를 표하십시오"))
love = 5000000000000000
while 1:
    print("축하합니다! 당신은 정답을 맞췄습니다. 현수는 확실히 그녀를 사랑합니다! %d" %love)
    love = love - 1
else:
    print("어디서 거짓말을 하고있어 %d" %love)
    love = love - 10

