#Map, filter

my_list=[1,2,3,4,5,6,7,8]

def multiplyBy2(item):
    return item*2

def only_odd(item):
    return item%2 != 0

print(list(map(multiplyBy2, my_list)))

print(list(filter(only_odd, my_list)))