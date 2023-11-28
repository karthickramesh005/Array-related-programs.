# Finding the frequency of element Frequency of elements in an array using Python :

def frequency(arr,n):
    for i in range(0,n):
        flag = False
        count = 0

        for j in range(i + 1,n):
            if arr[i] == arr[j]:
                flag = True
                break
        if flag == True :
            continue

        for j in range(0,i + 1):
            if arr[i] == arr[j]:
                count += 1
        print("{0}: {1}".format(arr[i], count))
            


arr = list(map(int,input("Enter a array elements : ").split()))
n = len(arr)
frequency(arr,n)
