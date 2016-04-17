for i in range (1,1000):
    for j in range (1,1000):
        if (1000-i-j)**2==i**2+j**2:
            print((1000-i-j)*i*j)
            break
