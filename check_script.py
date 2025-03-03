# Python program to check if a string starts with a given character using Lambda
starts_with = lambda s, c: s.startswith(c)

# Sample Inputs
input_string1 = "C#"
input_char1 = "C"
input_string2 = "Hello"
input_char2 = "O"

# Checking the strings
result1 = starts_with(input_string1, input_char1)
result2 = starts_with(input_string2, input_char2)

# Displaying the results
print(f"Input string '{input_string1}' and input character '{input_char1}' -> {result1}")
print(f"Input string '{input_string2}' and input character '{input_char2}' -> {result2}")
