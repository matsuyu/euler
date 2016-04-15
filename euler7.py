num=2
count=1
while count<10001:
    num+=1
    bool=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            bool=False
            break
    if bool:
        count+=1
print(num)
