"""if you have given a list,return the list with only even numbers"""
list1 = [3, 67, 54, 43, 72, 87, 98, 76, 53]
list_even = [i for i in list1 if i % 2 == 0]
print(*list_even)
