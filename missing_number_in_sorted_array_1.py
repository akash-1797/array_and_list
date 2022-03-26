def missing_numbers(arr):
  N = len(arr)
  b = [0]*(arr[N-1]+1)
  for i in range(N):
    b[arr[i]]=1
  for j in range(arr[0],arr[N-1]+1):
    if b[j]==0:
      print(j)

arr = [6,7,10,11,13]
missing_numbers(arr)
