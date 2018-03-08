for i in range(0,13):
    for j in range(0,13):
        if i==0 and j==0:
            my_str += "x".ljust(5," ")
        elif i==0:
            my_str += str(j).ljust(5," ")
        elif i>0 and j==0:
            my_str += str(i).ljust(5," ")
        else:
            my_str += str(i*j).ljust(5," ")
        if j==12:
            my_str += "\n"

print(my_str)
