#Highest even


def highest_even(my_list):
    even_list = []
    for item in my_list:
        if item % 2 ==0:
            even_list.append(item)
    return max(even_list)

print(highest_even([12,41,33,53,51,60,61]))