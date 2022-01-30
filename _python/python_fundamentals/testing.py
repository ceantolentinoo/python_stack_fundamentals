def biggie(y):
    for i in range(len(y)):
        if(y[i]<0):
            y[i]="big"
    return y

print(biggie([1,3,4,-5]))