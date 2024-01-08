# What is the expected output of the following code?
data = {'name': 'Peter', 'age': 30}
person = data.copy()
person2 = data
print(id(data))
print(id(person))
print(id(person2))


print(id(data) == id(person))


try:

    # print(int("hello")) # Value Error
    # print(int(1/0)) # Zero Division Error
    # print(10 + 'a') # Type Error
    x = 10
    print(x.append(4)) # Attribute Error No method called append in int datatype
except ValueError:
    print('Value Error')
except ZeroDivisionError:
    print('Zero Division Error')
except TypeError:
    print('Type Error')
except AttributeError:
    print('Attribute Error')
except Exception:
    print('Exception')



x = 1
print(++++x)

# There are no incrementers in python
x = 1
print(++++x)  # 1

print(+1)  # 1
print(++1)  # 1
print(+++1)  # 1
print(++++1)  # 1

print(-1)  # -1
print(--1)  # 1
print(---1)  # -1
print(----1)  # 1


def func():
    global x
    print('1. x:', x)
    x = 23
    print('2. x:', x)
x = 42
func()

print('3. x:', x)

"""
1. x: 42
2. x: 23
3. x: 23
"""

# What is the output of the following snippet?
# tup = (1, ) + (1, )
tup = (1, 1)
print(tup)       # (1, 1)
# tup = tup + tup
tup = (1, 1) + (1, 1)
print(tup)       # (1, 1, 1, 1)
print(len(tup))  # 4


# What is the expected output of the following code?
data = ((1, 2),) * 7
print(data)

#print(len(data[3:8]))

# What is the expected output of the following code?
data = {'one': 'two', 'two': 'three', 'three': 'one'}
res = data['three']
print(res)
for _ in range(len(data)):
    res = data[res]
print(res)