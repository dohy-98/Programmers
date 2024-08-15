rep = list(map(int,input().strip().split()))
rep_min = [rep[0],rep[1],rep[2]-rep[0],rep[3]-rep[1]]
print(min(rep_min))
