

i=0
board = ""
while i<10000:
    if i%2==0:
        board += " "
    elif i%2==1:
        board += "*"
    if i%41==0:
        board += "\n"

    i+=1
print(board)