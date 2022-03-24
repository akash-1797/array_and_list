def is_sorted(arr):
  n = len(arr)
  i = 0
  while(i<=n-2):
    if arr[i]>arr[i+1]:
      return False
    i = i+1
  return True

arr = [1,2,3,4,5]
print(is_sorted(arr))
