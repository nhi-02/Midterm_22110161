def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

a = list(map(int, input("input array: ").split()))

sort_a = bubble_sort(a)

print("sorted: ", sort_a)

