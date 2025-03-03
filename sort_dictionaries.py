#!/usr/bin/env python3

# Original list of dictionaries
list_of_dicts = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# Sorting the list of dictionaries by the 'model' key
sorted_list = sorted(list_of_dicts, key=lambda x: int(x['model']))

# Displaying the sorted list
print("Original list of dictionaries:")
print(list_of_dicts)
print("\nSorted list of dictionaries:")
print(sorted_list)
