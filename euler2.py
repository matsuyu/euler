a=[]
a.append(1)
a.append(2)
total=2
i=2
while a[i-1]+a[i-2]<=4000000:
    a.append(a[i-1]+a[i-2])
    if a[i]%2==0:
        total+=a[i]
    i+=1

print(total)
