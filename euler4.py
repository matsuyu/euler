number=1000000
bool=True
j=1
while bool:
    number-=1
    num=str(number)
    bool1=True
    for i in range (int(len(num)//2)):
        if num[i]!=num[len(num)-1-i]:
            bool1=False
    if bool1:
        for i in range(int(number**0.5),1000):
            if number%i==0 and number//i<1000:
                print(number)
                bool=False

