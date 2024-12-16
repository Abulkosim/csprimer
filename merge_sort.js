function mergeSort(arr) {
    if (arr.length <= 1) {
        return arr
    }

    const mid = Math.floor(arr.length / 2)
    
    let left = arr.slice(0, mid)
    let right = arr.slice(mid)

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)
}

function merge(left, right) {
    const result = []
    let i = 0
    let j = 0

    while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) {
            result.push(left[i])
            ++i
        } else {
            result.push(right[j])
            ++j
        }
    }

    result.push(...left.slice(i))
    result.push(...right.slice(j))

    return result    
}

const result = mergeSort([1, 3, 2, 10, 5, 6, 4, 7, 8, 9])
console.log(result)
