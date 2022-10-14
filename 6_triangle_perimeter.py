def get_triangle_perimeter(arr: list) -> int:
    arr.sort()
    arr.reverse()
    perimeter = 0
    for i in range(len(arr)-2):
        if arr[i] < arr[i+1] + arr[i+2]:
            perimeter = arr[i] + arr[i+1] + arr[i+2]
            break
    return perimeter


if __name__ == '__main__':
    n = input()
    inp_arr = [int(i) for i in input().split()]
    print(get_triangle_perimeter(inp_arr))
