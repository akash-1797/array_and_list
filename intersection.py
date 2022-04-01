def fun(arr,brr):
  c = []
  n1 = len(arr)
  n2 = len(brr)
  i = 0
  j = 0
  while(i<=n1-1 and j<=n2-1):
    if arr[i] < brr[j]:
      i = i+1
    elif arr[i] > brr[j]:
      j = j+1
    else:
      c.append(arr[i])
      i = i+1
      j = j+1
  return c
      


arr = [4,5,6,7]
brr = [2,3,4,5,6]
print(fun(arr,brr))

