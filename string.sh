double_char() {
    input="$1"
    output=""
    for (( i=0; i<${#input}; i++ )); do
        char="${input:$i:1}"
        output+="$char$char"
    done
    echo "$output"
}

# Examples
double_char "The"  # Output: 'TThhee'
double_char "AAbb"  # Output: 'AAAAbbbb'
double_char "Hi-There"  # Output: 'HHii--TThheerree'
