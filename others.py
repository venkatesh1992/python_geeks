""" == checks the value of both the elements
whereas 'IS' checks whether both the elements are pointing to same object or not (same memory location)
"""

a = 10
b = 10
print(a == b)
print(a is b)

print(id(a))
print(id(b))

list1 = []
list2 = []
print(list1 == list2)
print(list1 is list2)

print(id(list1))
print(id(list2))

