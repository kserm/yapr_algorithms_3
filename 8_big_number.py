def comparator(num1, num2):
    if len(num1) == len(num2):
        return int(num1) > int(num2)
    else:
        sum1 = num1 + num2
        sum2 = num2 + num1
        return int(sum1) > int(sum2)


def biggest_number(arr, comp):
    for i in range(1, len(arr)):
        item = arr[i]
        j = i
        while j > 0 and comp(item, arr[j-1]):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = item
    return ''.join(arr)


# if __name__ == '__main__':
#     n = int(input())
#     inp_list = [int(i) for i in input().split()]
#     print(biggest_number(inp_list))

inp_str = '15 56 2'
inp_list = [i for i in inp_str.split()]
print(inp_list)
print(biggest_number(inp_list, comparator))