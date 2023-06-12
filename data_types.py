a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))

# print(max.int)
l = [1, 'venki']
print(type(l))

s = "Venki"
s1 = 'a'
print(type(s))
print(type(s1))

t = (1, 3, "qbc")
print(type(t))

d = {a: 1, b: 2}
print(type(d))

s2 = "Hi I'm Venkatesh" \
     " I'm learning"
print(s2)

# if I want my string in multiple lines go with triple quotes
s3 = """Hi I'm doing good
 what about you"""
print(s3)

# we can access elements in string by using index, either positive or negative index
#  negative index will give elements from the last
# s = "Venki"
print(s[1])
print(s[0])
print(s[-1])

# we can select part of string by using slicing
# s2 = "Hi I'm Venkatesh" \
#     " I'm learning"
print(s2[5:10:2])  # characters from 5 to 10 in steps of 2
print(s2[::2])  # total string in steps of 2

l1 = [1, 2, 3, 4, 5]
print(l1)
print(l1[0])
print(l1[1])
# print(l1[7])  # if we give larger index which is not present, it will give list index out of range error
print(l1[-1])

t1 = ()
t2 = ('a',)
t3 = tuple('Venki')
print(t1)
print(t2)
print(t3)
t4 = tuple([1, 2, 3])
print(t4)
# t5 = tuple('venki', 't')  # tuple expects only one argument, built in tuple keyword
# print(t5) this will give error

# Booleans either True or False
print(type(True))
print(type(False))
# print(type(true))  # other than True or False, python will throw error for remaining

d1 = {'v': 1, 'b': 2}
print(d1['v'])
print(d1.get('b'))
print(d1.get('c'))  # if key doesn't exist it will give None


x = 10000000000000000000000000000000000000000000
x += 1
print(x)

z = 100 ** 100
print(type(z))  # there is no long type in python 3, int can accommodate any large number


