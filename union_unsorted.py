def union_in_unsorted(arr1,arr2):
  res_arr = []
  n1 = len(arr1)
  n2 = len(arr2)
  i = 0
  while(i<=n1-1):
    res_arr.append(arr1[i])
    i = i+1
  j = 0 
  while(j<=n2-1):
    if arr2[j] not in res_arr:
      res_arr.append(arr2[j])
    j = j+1

  return res_arr

arr1 = [4,2,5,7,1,8]
arr2 = [9,10,4,6,90]
print( union_in_unsorted(arr1,arr2))

