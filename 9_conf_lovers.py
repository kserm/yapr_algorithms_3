def get_ids(arr: list) -> list:
    ids = []
    uniq_ids = set(arr)
    for i in uniq_ids:
        ids.append([-arr.count(i), i])
    ids.sort()
    return ids


if __name__ == '__main__':
    n = input()
    inp_arr = [int(i) for i in input().split()]
    k = int(input())
    for i in get_ids(inp_arr)[:k]:
        print(i[1], end=' ')
