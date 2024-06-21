# t = ("TheTestingAcademy", "for", "TheTestingAcademy")
# print(set(t))
#
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# my_set = set1.union(set2)
# print(my_set)
#
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# my_set = set1.intersection(set2)
# print(my_set)
#
#
# # my_set = set1.difference(set2)
# my_set = set2.difference(set1)
# print(my_set)

s1 = {2, 4, 6}
s2 = {4, 6, 8}
my_set = s1.union(s2)
print(my_set)

my_set = s1.intersection(s2)
print(my_set)

my_set = s1.difference(s2)
print(my_set)

my_set = s2.difference(s1)
print(my_set)
