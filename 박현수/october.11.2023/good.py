#while문 이라는 반복문을 배울 예정

#자신이 원하는 변수 이름을 설정 hit에 0을 대입
hit = 0

while hit < 11:
    hit = hit + 1 #WHILE문이 반복 될 때마다 +1씩 증가
    print("나무를 %d번 찍었습니다." %hit) #문자열 포맷팅
    #print()문은 출력하는 함수, %d에 hit이라는 변수가 대입된다
    