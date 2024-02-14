num_list = [1, 3, 9, 2, 20, 5]

comparison = lambda x, y: x > y

def maximum(num_list, comparison):
    n = len(num_list)
    i = 1
    max = num_list[0]
    while i < n:
        # print(str(num_list[i]) + '>' +str(max))
        if comparison(num_list[i], max):
            max = num_list[i]
        i += 1
        #print(max)
    return max

print(maximum(num_list, comparison))