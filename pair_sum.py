def pair_sum(arr,k):
  n = len(arr)
  i = 0
  while(i<=n-1):
    j = i+1
    while(j<=n-1):
      if arr[i]+arr[j] == k:
        print(arr[i],arr[j])
      j = j+1
    i = i+1

arr = [6,3,8,10,16,7,5,2,9,14]
k = 9
print(pair_sum(arr,k))
