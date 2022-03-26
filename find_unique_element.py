idef unique(arr):
  n = len(arr)
  i = 0
  while (i <= n-1):
    for j in range(0,n):
       if (arr[i]==arr[j] and i != j):
         break
       j=j+1
    if (j == n):
       print("\nunique elements in an array is", arr[i])
    i=i+1


arr = [1,2,3,4,4,1]
unique(arr)
