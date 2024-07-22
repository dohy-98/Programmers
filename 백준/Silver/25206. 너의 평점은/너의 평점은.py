cnt_rep = 0
su = 0
grade = {'A+':4.5,'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0 }
for _ in range(20) :
    N = input().strip()
    if N[-1] == 'P' :
        pass
    elif N[-1] == 'F' :
        cnt_rep += float(N[-6:-3])
    elif N[-2:] in grade :
        num = float(grade[N[-2:]])
        cnt = float(N[-6:-5])
        cnt_rep += cnt
        su = su + num*cnt
result = (su/cnt_rep)
print("{:.6}".format(result))
