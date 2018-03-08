import random

def myfunc():
    print ("Starting the program...")
    j=0
    for i in range(1,5001):
        a = random.randint(0, 1)
        if a==0:
            j+=1
        print("Attempt #"+str(i)+": Throwing a coin... It's a head! ... Got", j ,"head(s) so far and", i-j ,"tail(s) so far")
    print("Ending the program, thank you!")

myfunc()    