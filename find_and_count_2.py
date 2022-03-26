def finding_and_counting_dups(arr):
  n = len(arr)
  b = [0]*(arr[n-1]+1)
  for i in range(0,n):
    b[arr[i]]= b[arr[i]]+1
  for j in range(arr[0],arr[n-1]+1):
    if b[j] > 1:
      print(j,b[j])

arr = [1,2,2,3,4,4,4]
print(finding_and_counting_dups(arr))
      
