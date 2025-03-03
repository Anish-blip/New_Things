# Python program to filter a list of integers using Lambda
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtering even numbers using lambda
even_numbers = list(filter(lambda x: x % 2 == 0, original_list))

# Filtering odd numbers using lambda
odd_numbers = list(filter(lambda x: x % 2 != 0, original_list))

# Displaying the results
print("Original list of integers:")
print(original_list)
print("\nEven numbers from the said list:")
print(even_numbers)
print("\nOdd numbers from the said list:")
print(odd_numbers)

