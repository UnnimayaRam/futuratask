def index(array, target):
    for index, num in enumerate(array):
        if num == target:
            return index
    return "not found"

target = 3
array = (1,4,5,7,9)

print(index(array,target))