def flatten_list(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

# Örnek Kullanım:
input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output = flatten_list(input_list)
print(output)

def reverse_elements(lst):
    reversed_list = []
    for item in lst:
        if isinstance(item, list):
            reversed_list.append(reverse_elements(item)[::-1])
        else:
            reversed_list.append(item)
    return reversed_list

# Örnek Kullanım:
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output = reverse_elements(input_list)
print(output)
