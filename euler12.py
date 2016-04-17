def factor(n):
    total=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            total+=2
    return total

i=1
number=0
while True:
    number+=i
    i+=1
    if factor(number)>500:
        print(number)
        break
