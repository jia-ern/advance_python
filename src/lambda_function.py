# ========= lambda function =========
def addition(x, y):
    return x+y

add = lambda x,y:x+y
print("lambda:", add(1, 2))

# ========= lambda with sorted() function =========
print("sorted:", sorted(['aaaa', 'bbb', 'cc']))
print("sorted with len as key:", sorted(['aaaa', 'bbb', 'cc'], key=len))

data = ['aaaa bbbb', 'bbb ccc', 'cc dd']
print('aaaa bbbb'.split()[1])

def split_func(name):
    return name.split()[1]
print("sorted with split:", sorted(data, key=split_func))

# lambda
print("sorted with split lambda:", sorted(data, key=lambda x:x.split()[1]))

# ========= nested lambda function =========
add = lambda x: lambda y:x+y
print("nested lambda: ", add(1))
# output: nested lambda:  <function <lambda>.<locals>.<lambda> at 0x00000284525A96C0>

# fix:
func = add(1)
print("Fixed nested lambda: ", func(2))

# ========= pass in lambda function =========
square = lambda n: n**2

def calculator(func):
    num=int(input("Enter a number: "))
    return func(num)

print("Pass in lambda:", calculator(square))

# ========= lambda function if else =========
num1 = 10
num2 = 20

if num1 > num2:
    print(num1)
else:
    print(num2)

print(num1 if num1 > num2 else num2)
comparison = lambda: num1 if num1 > num2 else num2
print("lambda if else: ", comparison())

