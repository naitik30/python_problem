data = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
# 13 14 15 16
t = 0
b = 3  #(m-1)
l = 0
r = 3 #(n-1)
dir =0
while t<=b and l<=r:
    if dir  ==0:
        for i in range(l,r+1):
            print(data[t][i])
        t +=1
        dir =  1
    if dir == 1:
        for i in range(t,b+1):
            # print(i)
            print(data[i][r])
        r-=1
        dir =2
    if dir == 2:
        for i in range(r,l-1,-1):
            print(data[b][i])
        b-=1
        dir =3
    if dir == 3:
        for i in range(b,t-1,-1):
            print(data[i][l])
        l +=1
        dir =0
# output

# 1
# 2
# 3
# 4
# 8
# 12
# 16
# 15
# 14
# 13
# 9
# 5
# 6
# 7
# 11
# 10
