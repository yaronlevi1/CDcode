
list_one = ['celeryss','carrots','bread']
list_two = ['celery','carrots','bread']

a=0
if len(list_one)==len(list_two):
    for i in range(0,len(list_one)):
        if list_one[i]!=list_two[i]:
            a=1
            break
else:
    a=1

if a==0:
    print("same")
elif a==1:
    print("not same")