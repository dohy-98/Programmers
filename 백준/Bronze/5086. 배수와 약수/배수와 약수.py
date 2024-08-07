while True :
    A,B = map(int,input().strip().split())
    if A == 0 and B == 0 :
        break
    else :
        if B/A == B//A :
            print("factor")
        elif A/B == A//B :
            print("multiple")
        else :
            print("neither")