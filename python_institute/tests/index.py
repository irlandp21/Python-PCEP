# from sys import argv
# sum = 0
# for i in range(2, len(argv)):
#     sum += float(argv[i])
# print(
#     "The average score for {0} is {1:.2f}"
#     .format(argv[1], sum/(len(argv)-2))
# )
#
# tup = (1, ) + (1, )
# tup = tup + tup
# print(len(tup))


def func(x=2, y=3):
    return x * y


print(func(y=2))

for ch in "adam_smit@openedg.org":

    if ch == "@":
        break

    print(ch, end="")

list = ['A', 2, 7, 1, 4]

list.reverse()
print(list)

data = [1, 2, 3, None, (), [], ]
print(len(data))

my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)


data = ((1, 2),) * 7
print(len(data[3:8]))

# x = 2
# y = 6
# x += 2 ** 3
# x //= y // 2 // 3
# print(x)
#
#
# def func(a, b):
#     return b ** a


# print(func(b=2, 2))

# data = [1, 2, [3, 4], [5, 6], 7, [8, 9]]
# count = 0
#
# for i in range(len(data)):
#     if type(data[i]) == list:
#         count += 1
#
# print("Count",count)
#
# num = float(input("Enter a number: "))
# print(int(num))
#
#
# data = ['abc', 'def', 'abcde', 'efg']
# print(max(data))
#
# x, y = eval(input('Enter two numbers: '))
# print(x)
# print(y)
#
# print('test')

data = ['Peter', 'Paul', 'Mary']
print(data[int(-1 / 2)])

y = 2 + 3 * 5.
print(y)


# data = [10, 2, 1, 7, 5, 6, 4, 3, 9, 8]
# # insert your code here
# print(
#     ('The highest number is {} ' +
#      'and the lowest number is {}.').format(high, low)
# )


for i in range(5, 0, -1):
    print(i, i, i, i, i)


