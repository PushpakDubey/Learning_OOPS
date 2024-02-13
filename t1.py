s = [8,7,6,5,3,5,9,4,0,2,3,4,3,1,6,3,8,3]
l = len(s)

for n1 in range(l-1):
    for n2 in range(0, l-n1-1):
        if s[n2] > s[n2+1]:
            s[n2], s[n2+1] = s[n2+1], s[n2]
print(s)