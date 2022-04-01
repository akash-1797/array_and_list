def rotation(arr,k):
  n = len(arr)
  z = n-k
  k =  k % n
  l = 0
  r = n-1
  while(l<r):
    arr[l],arr[r]=arr[r],arr[l]
    l = l+1
    r = r-1
  l = 0
  r = z-1
  while(l<r):
    arr[l],arr[r] = arr[r],arr[l]
    l = l+1
    r = r-1
  l = z
  r = n-1
  while(l<r):
    arr[l],arr[r] = arr[r],arr[l]
    l = l+1
    r = r -1
  return arr

arr = [1,2,3,4,5,6,7]
k =4
print(rotation(arr,k))
      
    
