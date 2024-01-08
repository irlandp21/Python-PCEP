list1 = [1,2,3,4,5]
list2 = [4,5,5,7,8]

set1 = set(list1)
set2 = set(list2)
print(set1)
print(set2)

print("Union - set1 | set2 (ie all elements in set1 or set2) ",set1 | set2)
print("Intersection - set1 & set2 (ie all elements in both set1 and set2) ",set1 & set2)
print("Difference - set1 - set2 (ie all elements in set1 that are not in set2) ",set1 - set2)
print("Difference - set2 - set1 (ie all elements in set2 that are not in set1) ",set2 - set1)
print("Symmetric Difference - set1 ^ set2 (ie all elements in set1 and set2 that don't intersect) ",set1 ^ set2)
