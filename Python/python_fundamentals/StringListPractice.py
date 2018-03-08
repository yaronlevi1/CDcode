words = "It's thanksgiving day. It's my birthday,too!"
print(words.find("day"))
words_alt = words.replace("day", "month", 1)
print(words_alt)

x = [2,54,-2,7,12,98]
print(min(x), max(x))

x = ["hello",2,54,-2,7,12,98,"world"]
print(x[0], x[len(x)-1])
x_alt = [x[0], x[len(x)-1]]
print(x_alt)

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print(x)
x0=x[0: int(len(x)/2)]
x1=x[int(len(x)/2):]
print(x0, x1)
x1.insert(0,x0)
print(x1)



# .find()
# .replace()
# min()
# max()
# .sort()
# len()