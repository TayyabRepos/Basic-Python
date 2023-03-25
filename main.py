#Tuples
#Tuples in immutable
my_tuples = (1,2,3,4,5,3,3,3)
new_tuples = my_tuples[1:2]
print(new_tuples)
print(my_tuples.index(4))
a,s,d,f ,*others = my_tuples
print(s)

