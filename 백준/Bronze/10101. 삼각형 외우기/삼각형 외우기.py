A = int(input())
B = int(input())
C = int(input())
if A+B+C == 180 :
    if A == B == C == 60 :
        print('Equilateral')
    else :
        if A == B or A == C or B == C :
            print('Isosceles')
        elif A != B and B != C and A != C :
            print('Scalene')
else :
    print('Error')