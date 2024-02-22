def find_longest_string(str_list):
    longest_str = max(str_list, key=len)
    return longest_str

input1 = ['cat', 'car', 'fear', 'center']
input2 = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
print(find_longest_string(input1))
print(find_longest_string(input2))
