list1 = [1, 3, 5, 7]
list2 = [3, 9, 4, 1]

intersection = list(filter(lambda x: x in list2, list1))

print(intersection)