def max_min(arr):
  n = len(arr)
  min = arr[0]
  max = arr[0]
  i = 0
  while(i<=n-1):
    if arr[i]<min:
      min = arr[i]
    elif arr[i]>max:
      max = arr[i]
    i = i+1
  return min , max 

arr = [6,3,8,10,16,7,5,2,9,4]
print(max_min(arr))
    
