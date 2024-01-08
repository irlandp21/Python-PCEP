data = [[42, 17, 23, 13], [11, 9, 3, 7]]
res = data[0][0]
print(res)
for da in data:
    print(da)
    for d in da:
        if res > d:
            res = d
#print(res)

# Which of the code snippet below will print the following to the monitor?
# Paul
# Mary
# Jane
da = ['Peter', 'Paul', 'Mary','Jane']
print(da[1:])

# What is the expected output of the following code?
x = (1, 4, 7, 9, 10, 11)
y = {2: 'A', 4: 'B', 6: 'C', 8: 'D', 10: 'E', 12: 'F'}
res = 1
for z in x:
    if z in y:
        print(z)
        res += z
print(res)




