l=list(map(str,input().split()))
for i in range(len(l)):
    if i%2==0:
        print(l[i][::-1],end=" ")
    else:
        print(l[i],end=" ")
