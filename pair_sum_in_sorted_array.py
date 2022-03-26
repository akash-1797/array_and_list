def pair_sum2(arr,k):
  n = len(arr)
  i = 0
  j = n-1
  while(i<j):
    if arr[i]+arr[j] == k:
      print(arr[i],arr[j])
      i = i+1
      j = j-1
    elif arr[i]+arr[j] < k:
      i = i+1
    else:
      j = j-1

arr = [1,3,4,5,6,8,9,10,12,14]
k =10 
print(pair_sum2(arr,k))
