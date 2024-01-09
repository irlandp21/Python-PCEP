print('Peter' 'Wellert')

data = {}


def func(d, key, value):
    d[key] = value


print(func(data, '1', 'Peter'))

data = [[0, 1, 2, 3] for i in range(2)]
# print(data[2][0])

#What is the expected output of the following code?
people = {}
def add_person(index):
    if index in people:
        people[index] += 1
    else:
        people[index] = 1


add_person('Peter')
add_person('Paul')
add_person('peter')
print(people)
print(len(people))


# What is the expected output of the following code?
x = 9
y = 12
result = x // 2 * 2 / 2 + y % 2 ** 3
print(result)


#What is the output of the following code?
try:
    # /value = input("Enter a value: ")
    # print(value/value)
    pass
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")

print(1 // 2 * 3)

# What is the expected output of the following code?
data = 'abbabadaadbbaccabc'
print(data.count('ab', 1))

# What is the output of the following snippet?
my_list = [x * x for x in range(5)]

def fun(lst):
    del lst[lst[2]]
    return lst


print(fun(my_list))

#What is the expected output of the following code?
def func(message, num=1):
    print(message * num)


func('Hello')
func('Welcome', 3)