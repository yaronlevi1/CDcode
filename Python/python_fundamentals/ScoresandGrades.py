import random

def myfunc():
    print ("Scores and Grades")
    for i in range(10):
        a = random.randint(60, 100)
        if a>=60 and a<70:
            b = "D"
        elif a>=70 and a<80:
            b = "C"
        elif a>=80 and a<90:
            b = "B"
        elif a>=90 and a<=100:
            b = "A"
        print("Score:",a,"; Your grade is ", b)
    print("End of program. Bye!")

myfunc()        
