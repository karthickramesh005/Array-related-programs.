# Removing Duplicates elements from an array :

arr = list(map(int,input("Enter a elements in array : ").split()))

unique_arr = []

for i in arr:
    if i not in unique_arr :
        unique_arr.append(i)

print(unique_arr)
