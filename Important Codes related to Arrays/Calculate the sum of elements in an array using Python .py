# Calculate the sum of elements in an array using Python :

def calculate(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        total += arr[i]
    return total
    


arr = list(map(int,input("Enter a array elements :   ").split()))
print("Sum of the value is : ",calculate(arr))
