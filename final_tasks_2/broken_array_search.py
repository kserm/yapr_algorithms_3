# 71562211

def broken_search(nums, target) -> int:
    start = 0
    stop = len(nums) - 1
    while start <= stop:
        middle = (start + stop) // 2
        if target == nums[middle]:
            return middle
        elif target == nums[start]:
            return start
        elif target == nums[stop]:
            return stop
        elif nums[start] > nums[middle]:
            if nums[middle] < target < nums[stop]:
                start = middle + 1
            else:
                stop = middle - 1
        else:
            if nums[start] < target < nums[middle]:
                stop = middle - 1
            else:
                start = middle + 1
    return -1
