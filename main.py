#Key in dictionary should be immutable
#Key in dictionary should be unique otherwise it will overwrite

dictionary={
    '12':[1,2],
    True: 'Hello',
    'is_Magic':False,
    # 'age': 100
}

print(dictionary.get('age',12))


# print(dictionary['12'])
# print(dictionary[True])
# print(dictionary['is_Magic'])