strings = ['Hello', 'Nope', 'Really', 'Good']

sorted_str = sorted(strings, key=lambda x: (len(x), x))

print(sorted_str)