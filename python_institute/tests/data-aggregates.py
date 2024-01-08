x = {(1, 2): 1, (2, 3): 2}

#a tuple can be the index of a dictionary
#And calling it you can (like often) leave out the parentheses.
print(x[1, 2])

for k in x:
    print("k=",k,"->",x[k])

# What is the expected output of the following code?
data = {'z': 23, 'x': 7, 'y': 42}

for _ in sorted(data):
    print(data[_], end=' ')
print()
data = [1, 5, 10, 19, 55, 30, 55, 99]
data.pop(5)
data.remove(19)
data.remove(55)
data.remove(55)
print(data)