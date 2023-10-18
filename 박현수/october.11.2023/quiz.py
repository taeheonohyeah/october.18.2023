print("두 가지 숫자를 입력 해 주세요")

num1 = int(input("첫 번째 숫자: "))
num2 = int(input("두 번째 숫자: "))

if num1 > num2:
    print("첫 번째 숫자가 두 번째 숫자보다 %d 큽니다" %(num1 - num2))
elif num2 > num1:
    print("두 번째 숫자가 첫 번째 숫자보다 %d 큽니다." %(num2 - num1))