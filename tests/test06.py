def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))

print( 9 // 3 -7)
print( 9 / 3 * 7)

res = str(bool(1) + float(12) / float(2))
print(res)

for i in range(5, 0, -1):
    print(i, i, i, i, i)

print('x', 'y', 'z', sep='sep')

x = 42
y = 7
data = "I'm gonna make him an offer he can't refuse."
r = data.rfind("an") if data else None
# r = 19 if None else x / y
# r = data.rfind('an') if data else None
# r = 7 if len(data) > 19 else 6
print(r)

# print(float("1, 3"))
#
# my_list = ['Mary', 'had', 'a', 'little', 'lamb']
#
#
# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'
#
#
# print(my_list(my_list))

# num = '7' * '7'
# print(num)

print('Mike' > 'Mikey')

data = (1, 2, 3, 4)
data = data[-2:-1]
data = data[-1]
print(data)

data1 = (1, 2)
data2 = (3, 4)
print([print(sum(x)) for x in [data1 + data2]])


def func(x, y, z):
    return x + 4 * y + 5 * z


print(func(1, z=2, y=3))


