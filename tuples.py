# Original list of tuples
tuples_list = [('C', 88), ('C++', 90), ('Java', 97), ('Python', 82)]

# Sorting the list of tuples using a lambda function
sorted_list = sorted(tuples_list, key=lambda x: x[1])

# Display the sorted list
print("Original list of tuples:", tuples_list)
print("Sorted list of tuples:", sorted_list)
