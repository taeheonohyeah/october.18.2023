#while문을 사용한 별삼각형 만들기
star = 0 #별의 갯수를 설정할 변수

while True:
    star = star + 1
    print("*"*star)

    if star == 177:
        break
    

star = 177
while True:
    star = star - 1
    print("*"*star)

    if star == 0:
        break