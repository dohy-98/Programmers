A = int(input())
B = int(input())
if -1000 <= A <= 1000 and A != 0 and -1000 <= B <= 1000 and B != 0 :
    if A > 0 and B > 0 :
        print(1)
    elif A < 0  and B > 0:
        print(2)
    elif A < 0 and B < 0:
        print(3)
    else :
        print(4)