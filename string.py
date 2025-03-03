def double_char(s):
    return ''.join([c*2 for c in s])

# Examples
print(double_char('The'))  # Output: 'TThhee'
print(double_char('AAbb'))  # Output: 'AAAAbbbb'
print(double_char('Hi-There'))  # Output: 'HHii--TThheerree'
