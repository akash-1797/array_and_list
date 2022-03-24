def arrange(arr):
  n = len(arr)
  i = 0
  j = n-1
  while(i<j):
    while(arr[i]<0):
      i =i+1
    while(arr[j]>=0):
      j = j-1
    if (i<j):
      arr[i],arr[j]=arr[j],arr[i]
    i = i+1
    j = j-1
  return arr


arr= [1,-2,-4,6,-6,7,8,4,-5]
print(arrange(arr))

