my_list = ['magical unicorns',19,'hello',98.98,'world']


my_str = "string:"
sum = 0
str_c = 0
num_c = 0
for i in my_list:
    if type(i)==str:
        my_str +=i+" "
        str_c+=1
    elif type(i)==int or type(i)==float:
        sum+=i
        num_c+=1

if str_c==0 and num_c==0:
    print("empty list")
elif str_c>0 and num_c==0:
    print("string only list")
elif str_c==0 and num_c>0:
    print("numbers only list")
elif str_c>0 and num_c>0:
    print("mixed list")

print(my_str)
print("sum: ", sum)