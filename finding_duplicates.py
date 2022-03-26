def finding_duplicates(arr):
  a = []
  n = len(arr)
  last_duplicate = 0
  i = 0
  while(i<=n-2):
    if arr[i] == arr[i+1] and arr[i] != last_duplicate:
      last_duplicate = arr[i]
      a.append(last_duplicate)
    i = i+1
  return a

arr = [1,2,2,3,4,4,5,5,5,5,6,6,7]
print(finding_duplicates(arr))

