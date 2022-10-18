glob_flag = False


def bubble_sort(input_list: list):
    ln = len(input_list)
    flag = False
    for i in range(ln-1):
        tmp_elem = input_list[i]
        if input_list[i] > input_list[i+1]:
            input_list[i] = input_list[i+1]
            input_list[i+1] = tmp_elem
            flag = True
            global glob_flag
            glob_flag = True
    if flag:
        for j in input_list:
            print(j, end=' ')
        print()
        bubble_sort(input_list)


if __name__ == '__main__':
    n = int(input())
    inp_list = [int(i) for i in input().split()]
    bubble_sort(inp_list)
    if glob_flag is False:
        for j in inp_list:
            print(j, end=' ')
