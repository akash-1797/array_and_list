def finding_and_counting_dups(arr):
  n = len(arr)
  i = 0
  while(i<=n-2):
    if arr[i] == arr[i+1]:
      j = i+1
      while (arr[i] == arr[j] and i <= n-2):
        j =j+1
        print(f'element {arr[i]} is appearing {j-i} times')
        i = j-1
    i = i+1

arr = [2,3,3,4,5,5,6,7,7]
print(finding_and_counting_dups(arr))
        
  
