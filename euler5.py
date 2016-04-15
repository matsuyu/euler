num=2
for i in range(2,21):
    number=num
    k=i
    j=1
    while j<=k:
        j+=1
        if k % j ==0 and number%j==0:
            k=k//j
            number=number//j
            j=1
    num*=k
print (num)
            
