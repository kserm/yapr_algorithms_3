def double_combinations(arr):
    n = len(arr)
    comb = []
    l_i = list(range(n))
    l_j = list(range(n))
    for i in l_i:
        for j in l_j:
            flag = False
            for item in comb:
                if i in item and j in item:
                    flag = True
                    break
            if flag == False and i != j:
                comb.append((i, j))
    return comb


def rec_combinations(len_arr):
    pass


def area_diff(arr: list, k: int) -> int:
    area = []
    comb = double_combinations(arr)
    for item in comb:
        i, j = item
        area.append(abs(arr[i]-arr[j]))
    sorted_area = sorted(area[:k])
    # return sorted_area[-1]
    print(sorted_area)
    return sorted(area)


# if __name__ == '__main__':
#     n = input()
#     inp_arr = [int(i) for i in input().split()]
#     k = int(input())
#     print(area_diff(inp_arr, k))

inp_arr = [1, 3, 5, 6, 8]
k = 3

print(area_diff(inp_arr, k))
print(double_combinations(inp_arr))