num_list = [1,2, 3, 4, 5, 6]

def even_number(num):
    if num % 2 == 0:
        return True
    else:
        return False

filtered_object = filter(even_number, num_list)
print(filtered_object)  # filter() function works and Python's use of lazy evaluation
print(list(filtered_object)) # Python eagerly evaluates the filter object and retrieves all the qualifying elements

# =========== filter() with lambda ===========
filtered_object = filter(lambda x: True if x%2==0 else False, num_list)
print("filter with lambda: ", list(filtered_object))