'''
list1 = [1, 2, 3]
list2 = [3, 4, 5]
set1 = set(list2)
set2 = set(list1)
set1.update(set2)
print(set1)
set1.update(list2)
print(set1)
 Output:
1 2 3 4 5
'''
