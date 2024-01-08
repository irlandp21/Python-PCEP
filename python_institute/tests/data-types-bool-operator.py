# By default, an object is considered true unless its class defines either a __bool__() method that returns False or a __len__() method that returns zero, when called with the object. Here are most of the built-in objects considered false:
#
# constants defined to be false: None and False.
# zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# empty sequences and collections: '', (), [], {}, set(), range(0)

print("bool(0)",bool(0))
print("not 0",not 0)
print("bool([])",bool([]))
print("not []",not [])
print("bool([1,2,3])",bool([1,2,3]))
print("not [1,2,3])",not [1,2,3])
print("bool(23)",bool(23))
print("not 23",not 23)
print("bool(\'\')", bool(''))
print("not \'\'", not '')
print("bool(\'Peter\')",bool('Peter'))
print("not \'Peter\'",not 'Peter')
print("bool(None)",bool(None))
print("not None",not None)

print(not [])
print(not set())

print(not None)