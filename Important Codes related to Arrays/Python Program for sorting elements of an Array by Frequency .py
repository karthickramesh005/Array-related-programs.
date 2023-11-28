# Python Program for sorting elements of an Array by Frequency :

from collections import Counter
from itertools import repeat, chain
ini_list =list(map(int,input("Enter a array elements : ").split()))

# sorting on bais of frequency of elements
result = sorted(ini_list, key = ini_list.count, reverse = True)

# printing final result
print(str(result))
