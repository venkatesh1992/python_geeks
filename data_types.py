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
