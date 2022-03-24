def rev(arr):
  n = len(arr)
  temp = 0
  i = 0
  j = n-1
  while(i<=j):
    temp = arr[i]
    arr[i]=arr[j]
    arr[j] = temp
    i = i+1
    j = j-1
  return arr

arr = [1,2,3,4,5,6]
print(rev(arr))
