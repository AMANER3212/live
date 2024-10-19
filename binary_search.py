def binary_r(arr, left, right, target, steps=0):
    if left > right:
        return -1, steps
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid, steps
    elif arr[mid] < target:
        return binary_r(arr, mid + 1, right, target, steps + 1)
    else:
        return binary_r(arr, left, mid - 1, target, steps + 1)

def binary_search(arr, left, right, target):
    index, steps = binary_r(arr, left, right, target, 0)
    if index != -1:
        print(f"Element found at {index}")
    else:
        print("Element not found")

arr = [10, 20, 30, 40, 50]
binary_search(arr, 0, len(arr) - 1, 30)

def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

x = binary_search_iterative(arr, 40)
print(x)
