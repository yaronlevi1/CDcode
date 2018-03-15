
def bubble(arr):
    print(arr)
    z=0
    while z == 0:
        for i in range(1,len(arr)):
            if arr[i]<arr[i-1]:
                break
            elif i == len(arr)-1:
                z=1
        for j in range(1,len(arr)):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    print(arr, "Done")
    return arr

    
bubble([13,12,11,9,1])
        