# Original list of dictionaries
original_list = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# Sorting the list of dictionaries by the 'make' key
sorted_list = sorted(original_list, key=lambda x: x['make'])

# Displaying the sorted list
print("Original list of dictionaries:")
print(original_list)
print("\nSorting the List of dictionaries:")
print(sorted_list)

