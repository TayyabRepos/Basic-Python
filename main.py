#for loop

# for item in [1,2,3,4,5,6,7,8,9,10]:
#     for x in ['a','b','c']:
#         print(item,x)

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}
for item in user:
    print(item)

print('_________')
for item, value in user.items():
    print(item, value)
print('_________')
for item in user.values():
    print(item)
print('_________')
for item in user.keys():
    print(item)