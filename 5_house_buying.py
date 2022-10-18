def get_houses(n: int, budget: int, house_list: list) -> int:
    counter = 0
    s = 0
    house_list.sort()
    for h in house_list:
        s += h
        if s <= budget:
            counter += 1
    return counter


if __name__ == '__main__':
    n, bdgt = [int(i) for i in input().split()]
    house_list = [int(i) for i in input().split()]
    print(get_houses(n, bdgt, house_list))

n, bdgt = 3, 1000
house_list = [350, 999, 200]
print(get_houses(n, bdgt, house_list))
