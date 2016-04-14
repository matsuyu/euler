num=600851475143
i=1
while i<=num**0.5:
    i+=1
    if num%i==0:
        num=num//i
        i=1
print(num)
