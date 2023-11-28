# Find Largest element in an array using Python :

a = list(map(int,input("Enter a array elements : ").split()))

max_element = a[0]

for i in range(len(a)):
  if a[i] > max_element:
     max_element = a[i]

print (max_element)
