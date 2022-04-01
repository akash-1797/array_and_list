def right_rotation(arr,shift):
  n = len(arr)
  temp = 0
  i = 0
  while(i<shift):
    temp = arr[n-1]
    j = n-1
    while(j>=1):
      arr[j] = arr[j-1]
      j = j-1
    arr[0] = temp
    i = i+1
  return arr

arr = [1,2,3,4,5]
print(right_rotation(arr,2))
      
      
