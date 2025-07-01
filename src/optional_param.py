# pass in param
def func(word, frequency=1):
    return word * frequency
call = func('Hi', 5)
print(call)

# default frequency
def func_default_frequency(word, frequency=1):
    return word * frequency
call = func_default_frequency('Hi')
print(call)

