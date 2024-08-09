while True :
    N = int(input())
    if N == -1 :
        break
    else :
        rep = []
        su = 0
        for i in range(1,N+1):
            if N%i == 0 :
                rep.append(str(i))
                su += i

        rep.remove(rep[-1])
        su = su - N 
        txt = " + ".join(rep)

        if su == N :
            print(str(N) + ' = ' + txt)
        else :
            print(str(N) + ' is NOT perfect.')