def merge(arr1,arr2):
  arr3 = []
  i = 0
  j = 0
  len_1 = len(arr1)
  len_2 = len(arr2)
  while((i<len_1) and (j<len_2)):
    if arr1[i] < arr2[j]:
      arr3.append(arr1[i])
      i = i+1
    elif arr1[i] == arr2[j]:
      arr3.append(arr1[i])
      i = i+1
      j = j+1
    else:
      arr3.append(arr2[j])
      j = j+1
  while(i<len_1):
    arr3.append(arr1[i])
    i = i+1
  while(j<len_2):
    arr3.append(arr2[j])
    j = j+1
  return arr3

arr1 = [3,4,5,6,10]
arr2 = [2,4,5,7,12]
print(merge(arr1,arr2))

