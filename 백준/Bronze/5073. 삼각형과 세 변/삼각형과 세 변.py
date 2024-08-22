def classify_triangle(a, b, c):
    # 세 변이 삼각형을 만들 수 있는지 확인
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"
    # 세 변의 길이가 모두 같은 경우
    if a == b == c:
        return "Equilateral"
    # 두 변의 길이만 같은 경우
    if a == b or b == c or a == c:
        return "Isosceles"
    # 세 변의 길이가 모두 다른 경우
    return "Scalene"

# 예제 입력을 처리하는 코드
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    print(classify_triangle(a, b, c))
