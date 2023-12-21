def guesses(target, min, max):
    left, right = min, max
    while left <= right:
        mid = left + (right - left) // 2
        if mid == target:
            return mid
        if mid < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1