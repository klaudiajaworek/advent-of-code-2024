import numpy as np

def lists_distance(list1, list2):
    return sum(abs(np.sort(list1) - np.sort(list2)))

def similarity_score(list1, list2):
    values, counts = np.unique(list2, return_counts=True)
    count_dict = dict(zip(values, counts))
    return sum(elem * count_dict[elem] if elem in count_dict.keys() else 0 for elem in list1)


data = np.loadtxt("1/input.txt")
list1 = data[:, 0]
list2 = data[:, 1]
print(lists_distance(list1, list2))
print(similarity_score(list1, list2))