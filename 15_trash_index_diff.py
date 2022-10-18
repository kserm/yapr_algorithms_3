def double_ended_area_diff(arr: list, k: int) -> int:
    def _pairs(arr: list, dif: int) -> int:
        i, j, cnt, n = 0, 0, 0, len(arr)
        for i in range(len(arr)):
            while arr[i] - arr[j] > dif and j < i:
                j += 1
                cnt += (n-i)
        return n * (n-1) // 2 - cnt
    arr.sort()
    left, right = (
        min(arr[i+1] - arr[i] for i in range(len(arr)-1)),
        arr[-1] - arr[0]
    )
    while left <= right:
        mid = left + ((right - left) >> 1)
        if k <= _pairs(arr, mid):
            right = mid - 1
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    n = input()
    inp_arr = [int(i) for i in input().split()]
    k = int(input())
    print(double_ended_area_diff(inp_arr, k))
