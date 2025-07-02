names = ['aa', 'bbb', 'cccc']

def find_length(names):
    return len(names)

mappped_obj = map(find_length, names)
print(list(mappped_obj))
print(type(mappped_obj))

# ========== use map to add ============
num1 = [10, 20, 30]
num2 = [10, 20, 30]

def addition(num1, num2):
    return num1+num2

mappped_obj = map(addition, num1, num2)
print("addition with map: ", list(mappped_obj))

# ========== use map to add ============
laptops = {'hp': 10000, 'lenovo': 20000, 'mac': 60000}
budget = 50000

def filter_laptops(laptop):
    if laptops[laptop] < budget:
        return True
    else:
        return False

filtered_obj = filter(filter_laptops, laptops)
print("filtered laptops: ", list(filtered_obj))

