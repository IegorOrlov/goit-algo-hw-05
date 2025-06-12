def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iteration = 0

    while low <= high:
        iteration = iteration + 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return (iteration, x)

    return (iteration, arr[mid] if arr[mid] > x else arr[mid + 1])


arr = [2.3, 3.4, 4.2, 10.1, 40.5]
x = 3.1
result = binary_search(arr, x)
print(f"Кількість етерацій: {result[0]}, верхня межа: {result[1]}")