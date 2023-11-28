# Finding Repeating elements in an Array in Python :

def find_repeating_elements_set(arr):
    seen = set()
    repeating_elements = set()
    
    for element in arr:
        if element in seen:
            repeating_elements.add(element)
        else:
            seen.add(element)

    return list(repeating_elements)

# Example
my_array = list(map(int,input("Enter a array elements : ").split()))
repeating_elements = find_repeating_elements_set(my_array)
print("Repeating elements:", repeating_elements)
