function quicksort(arr, start = 0, end = arr.length - 1) {
    if (start < end) {
        let pivot_pos = partition(arr, start, end)
        quicksort(arr, start, pivot_pos - 1)
        quicksort(arr, pivot_pos + 1, end)
    }

    return arr
}

function partition(arr, start, end) {
    let randomPivotIndex = Math.floor(Math.random() * (end - start + 1)) + start
    let temp = arr[end]
    arr[end] = arr[randomPivotIndex]
    arr[randomPivotIndex] = temp

    let pivot = arr[end]
    let i = start - 1
    let j = start
    for (j; j < end; j++) {
        if (arr[j] <= pivot) {
            i++
            let temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        }
    }

    temp = arr[i + 1]
    arr[i + 1] = arr[end]
    arr[end] = temp
    return i + 1
}

console.log(quicksort([1, 3, 2, 10, 5]))