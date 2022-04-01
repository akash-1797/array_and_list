def left_array_rotation(arr,shift):
  n = len(arr)
  temp = 0
  i = 0
  for i in range(0,shift):
    temp = arr[0]
    j = 0
    while(j<=n-2):
      arr[j] = arr[j+1]
      j = j+1
    arr[n-1] = temp
  return arr
arr = [1,2,3,4,5,6,7,8,9,10]
print(left_array_rotation(arr,5))
    
    
