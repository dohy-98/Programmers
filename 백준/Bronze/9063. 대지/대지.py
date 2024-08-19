N = int(input())
A_rep = []
B_rep = []
for _ in range(N) :
    A,B = map(int,input().split())
    A_rep.append(A)
    B_rep.append(B)
print((max(A_rep)-min(A_rep))*(max(B_rep)-min(B_rep)))