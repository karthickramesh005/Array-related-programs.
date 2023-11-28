# Find non-repeating elements in an array Python :

def find_non_repeating_elements_set(arr):
    seen = set()
    repeating_elements = set()

    for element in arr:
        if element in seen:
            repeating_elements.add(element)
        else:
            seen.add(element)

    non_repeating_elements = list(set(arr) - repeating_elements)
    return non_repeating_elements

# Example
my_array = list(map(int,input("Enter a array elements : ").split()))
non_repeating_elements = find_non_repeating_elements_set(my_array)
print("Non-repeating elements:", non_repeating_elements)


