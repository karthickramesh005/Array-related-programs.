# Python program to count numbers of even and odd elements in an array :

arr = list(map(int,input("Enter a elements in array : ").split()))
n = len(arr)

evencount = 0
oddcount = 0
even =list()
odd = list()

for i in range(0,n):
    if arr[i] % 2 == 0 :
        even.append(i)
        evencount += 1
    else :
        odd.append(i)
        oddcount += 1

print("Number of Even numbers : ",evencount," are : ",even)
print("Number of Odd numbers : ",oddcount," are : ",odd)
