# Dictionary is unorderd key paird value

dictionary = {
    'a': [1, 2, 3],
    'b': 'Hello',
    'c': True
}

new_list = [
    {
        'a': [1, 2, 3],
        'b': 'Hello',
        'c': True
    },
    {
        'a': [4, 5, 6],
        'b': 'Hello',
        'c': True
    },
    {
        'a': [7, 6, 9],
        'b': 'Hello',
        'c': True
    }
]

list = new_list[0]['a'][2]
print(list)
