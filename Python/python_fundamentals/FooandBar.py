
for i in range(1,101):
    isPrime = 1
    isSq = 0
    for j in range(2,i-1):
        if i%j==0:
            isPrime = 0
    if i**0.5 == round(i**0.5):
        isSq=1


    if isPrime==1:
        print(i,":: Foo ::", "prime")
    elif isSq==1:
        print(i,":: Bar ::", " perfect")
    elif isPrime==0 & isSq==0:
        print(i,":: FooBar ::", "neither prime nor perfect")
        
        
    