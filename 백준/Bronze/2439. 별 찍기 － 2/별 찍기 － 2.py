N = int(input().strip())
if 1 <= N <= 100 :
    for i in range(N) :
        print(("*"*int(i+1)).rjust(N))