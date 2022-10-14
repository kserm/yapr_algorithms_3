def get_flowerbeds(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    arr.sort()
    arr.reverse()
    j = len(arr) - 1
    while j > 0:
        print(j)
        a = arr[j][0]
        b = arr[j][1]
        if arr[j-1][0] >= a and arr[j-1][1] <= b:
            arr.pop(j-1)
        elif a <= arr[j-1][0] and arr[j-1][0] <= b <= arr[j-1][1]:
            arr[j-1][0] = a
            if b >= arr[j-1][1]:
                arr[j-1] = b
            arr.pop()
        j -= 1
    arr.sort()
    return arr


if __name__ == '__main__':
    n = int(input())
    inp_arr = []
    for i in range(n):
        item = [int(i) for i in input().split()]
        inp_arr.append(item)
    for item in get_flowerbeds(inp_arr):
        for i in item:
            print(i, end=' ')
        print()
