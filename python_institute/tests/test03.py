# What is the expected output of the following code?
data = {'a': 1, 'b': 2, 'c': 3}
# print(data['a', 'b'])

#What is the expected output of the following code?

data = [1, {}, (2,), (), {3}, [4, 5]]
points = 0

for i in range(len(data)):
    if type(data[i]) == list:
        points += 1
    elif type(data[i]) == tuple:
        points += 10
    elif type(data[i]) == set:
        points += 100
    elif type(data[i]) == dict:
        points += 1000
    else:
        points += 10000

print(points)


# What is the expected output of the following code?
data = (1, 2, 4, 8)
data = data[1:-1]
data = data[0]
print(data)

nums = [1, 2, 3]
data = ('Peter',) * (len(nums) - nums[::-1][0])
print(data)


def any():
    print(var + 1, end='')
var = 1
any()
print(var)

#How many stars will the following snippet print to the monitor?
data = [[x for x in range(y)] for y in range(3)]

for d in data:
    if len(d) < 2:
        print('*')

#You want to print each name of the list on a new line.



data = ['Peter', 'Paul', 'Mary', 'Jane']
# print(data.concatenate("\n"))

L = [i for i in range(-1, -2)]
print(len(L))

x = 'Peter Wellert'
y = 'Peter Wellert'.lower()
print(x is y)

print('t' in 'Peter')
x=42
y=42
print(x is not y)

print('is' in 'This IS Python code')

x = ['Peter','Paul','Mary']
y = ['Peter','Paul','Mary']
print(x is y)

print(len([i for i in range(0, -2)]))