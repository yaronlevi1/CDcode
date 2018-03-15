
def push_front(arr, val):
  arr.append(None)
  for i in range(len(arr)-1,0,-1):
    arr[i]=arr[i-1]
  arr[0]=val
  print(arr)
  return arr
 
push_front([11,12,13,14], 9)



  