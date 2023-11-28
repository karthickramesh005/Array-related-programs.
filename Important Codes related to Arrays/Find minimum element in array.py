# Find minimum element in array :

arr = list(map(int,input("Enter a array elemets : ").split()))
mini = arr[0]

for i in range(len(arr)):
  if arr[i] < mini:
     mini = arr[i]

print (mini)
