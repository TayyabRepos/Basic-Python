#set and dictionary comprehention

# set1 = {char for char in 'hello'}
# set2 = {num for num in range(1,101)}
# set3 = {num**2 for num in range(1,101)}
# set4 = {num for num in range(1,101) if num%2 ==0}
#
# print(set1)
# print(set2)
# print(set3)
# print(set4)


# items1={
#     'a': 1,
#     'b': 2
# }
#
# my_dict = {key:value**2   for key,value in items1.items()}

my_dict = {num:num+1 for num in [1,2,3,4,5,6,7,8,9]}

print(my_dict)



