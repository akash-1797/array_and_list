def leader(arr):
  a = []
  n = len(arr)
  max = arr[n-1]
  a = [arr[n-1]]
  i = n-2
  while(i>=0):
    if arr[i] > max:
      a.append(arr[i])
      max = arr[i]
    i = i-1
  print(a)
  for i in range(len(a)-1,-1,-1):
    print(a[i],end=' ')

arr = [15,18,5,3,6,2]
leader(arr)

