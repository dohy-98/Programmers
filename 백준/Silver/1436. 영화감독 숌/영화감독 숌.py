N = int(input())  # 입력받는 값 N

count = 0         # "666"이 들어간 숫자를 카운트할 변수
number = 666      # 처음 시작하는 숫자

while True:
    # 현재 숫자에 "666"이 포함되어 있는지 확인
    if '666' in str(number):
        count += 1
    
    # N번째 숫자를 찾으면 출력하고 종료
    if count == N:
        print(number)
        break
    
    # 숫자를 증가시킴
    number += 1