
# 15 + 3 / 4 * 10 ** 2 ** 2

# 15 + 3 / 4 * 10 ** 4
# 15 + 3 / 4 * 10000
# 15 + 0.75 * 10000
# 15 + 7500.0
# 7515.0

print(15 + 3 / 4 * 10 ** 2 ** 2)


a = 1
b = 0
print("a=",a,"b=",b)
print("a = a ^ b =>",a,"^", b,"=",a^b)
a = a ^ b

b = a ^ b
print("b = a ^ b =>",a,"^", b,"=",a^b)

b = a ^ b
print(a, b)

# What is the expected output of the following code?
list1 = ['Peter', 'Paul', 'Mary', 'Jane']
list2 = ['Peter', 'Paul', 'Mary', 'Jane']

print(list1 is not list2)
print(list1 != list2)

list1 = list2

print(list1 is not list2)
print(list1 != list2)

