# Unpacking of tuple
a, b, c = (44, 55, 66)

t = (44, 55, 66)
# t.appned() # tuple are immutable in nature
new_t =  t + (77,)
print(new_t)

my_list = list(t)
print(my_list)
my_list.append(5)
new_t2 = tuple(my_list)
print(new_t2)
#

#Practise----------------------------------
# t = ( 2, 4, 6, 8)
#
# my_list = list(t)
# print(my_list)
# my_list.append((10))
# t2 = tuple(my_list)
# print(t2)