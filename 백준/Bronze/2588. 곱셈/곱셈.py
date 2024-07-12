A = int(input().rstrip())
B = int(input().rstrip())
if 100 <= A <= 999 and 100 <= B <= 999 :
    rep_B = [int(i) for i in str(B)]
    print(A * rep_B[2])
    print(A * rep_B[1])
    print(A * rep_B[0])
    print(A * B)