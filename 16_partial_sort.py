def get_segments_num(arr: list, bn=0):
    b_min = min(arr)
    start = 0
    stop = len(arr)
    for i in range(start, stop):
        if arr.index(b_min) == stop-1:
            bn += 1
            return bn
        else:
            if i < stop - 1:
                left_max = max(arr[start:i+1])
                right_min = min(arr[i+1:stop])
                if right_min > left_max:
                    bn += 1
                    start = i+1
                    b_min = right_min
            else:
                bn += 1
    return bn


if __name__ == '__main__':
    n = int(input())
    inp_arr = [int(i) for i in input().split()]
    print(get_segments_num(inp_arr))
