def binarySearch(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if x > arr[mid]:
        return binarySearch(arr, x, mid+1, right)
    if mid >= 1:
        if x <= arr[mid] and x <= arr[mid-1]:
            return binarySearch(arr, x, left, mid)
    else:
        if x <= arr[mid]:
            return mid+1
    return mid+1


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    x = int(input())
    index = binarySearch(arr, x, left = 0, right = len(arr))
    index_2 = binarySearch(arr, 2*x, left = 0, right = len(arr))
    print(index, index_2)
