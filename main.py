# List slicing
# lists are mutable, so we can change the values of the list
amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
amazon_cart[0] = 'laptop'
# print(amazon_cart[0::2])  # amazon_cart create a new list
# print(amazon_cart)

new_cart = amazon_cart  # Here we are not creating a new list instead we are just referencing the list
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

new_cart2 = amazon_cart[:]  # copy the list here we are creating a new list
print(new_cart2)
