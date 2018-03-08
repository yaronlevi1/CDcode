def odd_even():
    for i in range(1,21):
        if i%2==0:
            p2="even"
        else:
            p2="odd"
        print("NUmber is ",i, "-- This is an", p2, "number")
odd_even()

def multiply(a,b):
    mList=[]
    for i in a:
        mList.append(i*b)
    #print(mList)
    return mList
multiply([1,2,3],3)

def layered_multiples(arr):
    zz=[]
    for i in range(len(arr)):
        zz.append([1]*arr[i])
    print(zz)
    return zz
layered_multiples(multiply([2,4,5], 3))
