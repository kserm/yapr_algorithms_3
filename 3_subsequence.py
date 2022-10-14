def is_subsequence(str1, str2):
    l_str1 = len(str1)
    l_str2 = len(str2)
    if l_str1 > l_str2:
        return False
    i = 0
    for j in range(l_str2):
        if str1[i] == str2[j]:
            i += 1
            if i == l_str1:
                break
    return i == l_str1


str_1 = 'abc'
str_2 = 'ahbgdcu'

print(is_subsequence(str_1, str_2))
# if __name__ == '__main__':
#     str_1 = input()
#     str_2 = input()
#     print(is_subsequence(str_1, str_2))
