digits = int(input())
digits_str = str(digits)
digits_list = [i for i in digits_str]

sum = lambda x, y: x + y

while len(digits_list) > 1:
    i = int(digits_list.pop())
    j = int(digits_list.pop())
    digits_list.append(sum(i, j))
print(digits_list[0])