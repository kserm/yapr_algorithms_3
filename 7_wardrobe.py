def sort_wardrobe(arr):
    pink = []
    yellow = []
    crimson = []
    for i in arr:
        if i == '0':
            pink.append('0')
        elif i == '1':
            yellow.append('1')
        elif i == '2':
            crimson.append('2')
    return pink + yellow + crimson


if __name__ == '__main__':
    n = int(input())
    inp_arr = input().split()
    print(' '.join(sort_wardrobe(inp_arr)))
