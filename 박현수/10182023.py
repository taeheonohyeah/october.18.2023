#5명의 학생의 성적을 입력받아 학급 점수의 평균을 구하는

#학생의 수를 카운트할 변수 num
num = 0
#평균을 저장할 변수 result
result = 0

while True: #무한루프
    std = int(input("학생의 성적을 입력하세요"))
    num = num + 1
    result = result + std
    if(num ==5):
        print(result/num)
        break