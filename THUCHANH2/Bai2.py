def intersection(num_list1, num_list2):
    set1 = set(num_list1)
    set2 = set(num_list2)
    return list(set1.intersection(set2))

num_list1 = [1, 2, 3, 4, 5]
num_list2 = [3, 4, 5, 6, 7]
a = intersection(num_list1, num_list2)
print(a)
