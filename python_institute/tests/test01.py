print(list('hello'))  # ['h', 'e', 'l', 'l', 'o']

x = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

# def func(data):
#     print(data)
#     res = data[0][0]
#     for da in data:
#         for d in da:
#             if res < d:
#                 res = d
#     return res
#
#
# print(func(x[0]))

# What is the expected output of the following code?
z = y = x = 1
print(x, y, z, sep='*')


z = y = x = 1
print(x, y, z, sep='*')

# How many stars will the following snippet print to the monitor?
i = 4
while i > 0:
    i -= 2
    print('*')
    if i == 2:
        break
else:
    print('*')

# What is the expected output of the following code?
num = 1
def func():
    num = num + 3
    print(num)

func()

print(num)

# What is the expected output of the following code?
x = True
y = False
z = False

if not x or y: #False
    print(1)
elif not x or not y and z: #False or (not(False) and False) = False or False
    print(2)
elif not x or y or not y and x: #False or False or True and True
    print(3)
else:
    print(4)

