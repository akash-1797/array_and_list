def missing(arr):
  a = []
  n = len(arr)
  diff = arr[0]-0
  i = 0
  while(i<=n-1):
    if arr[i]-i != diff:
      while(diff < arr[i]-i):
        a.append(i+diff)
        diff = diff+1
    i = i+1
  return a

arr = [6, 7, 10, 11, 13]
print(missing(arr))
        
