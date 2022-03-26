def fun(arr):
  n = len(arr)
  i = 0
  while(i<=n-2):
    count = 1
    if arr[i] != -1:
      j = i+1
      while(j<=n-1):
        if arr[i] == arr[j]:
          count = count +1
          arr[j] = -1
        j = j+1
    if count > 1:
      print(arr[i],count)
    i = i+1

arr = [8,3,6,4,6,5,6,8,2,7]
print(fun(arr))
