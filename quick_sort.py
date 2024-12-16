def quicksort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    if start < end:
        pivot_pos = partition(arr, start, end)

        quicksort(arr, start, pivot_pos - 1)
        quicksort(arr, pivot_pos + 1, end)

    return arr


def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1