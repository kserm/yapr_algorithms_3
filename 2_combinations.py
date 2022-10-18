KEYBOARD_MAPPING = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}


def keyboard_combinations(numbers):
    if numbers == '':
        return ['']
    res = []
    letters = KEYBOARD_MAPPING[int(numbers[-1])]

    for combination in keyboard_combinations(numbers[:-1]):
        for char in letters:
            res.append(combination + char)
    return res


if __name__ == '__main__':
    inp_num = input()
    for item in keyboard_combinations(inp_num):
        print(item, end=' ')
