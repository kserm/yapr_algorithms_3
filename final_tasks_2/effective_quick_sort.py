# 71568041

from typing import List, Any


class Competitor:
    def __init__(self, login, solved, penalty):
        self.login = login
        self.solved = solved
        self.penalty = penalty

    def __lt__(self, competitor):
        return (
            (-self.solved, self.penalty, self.login) <
            (-competitor.solved, competitor.penalty, competitor.login)
        )

    def __str__(self):
        return self.login


def quick_sort(arr: List[Any], arr_length: int) -> List[Any]:

    def _quick_sort(start: int, end: int):
        if start >= end:
            return
        left = start
        right = end
        pivot = arr[(right + left) // 2]
        while left <= right:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        _quick_sort(start, right)
        _quick_sort(left, end)

    _quick_sort(0, arr_length - 1)
    return arr


def main():
    n = int(input())
    inp_arr = []
    for _ in range(n):
        login, solved, penalty = input().split()
        inp_arr.append(Competitor(login, int(solved), int(penalty)))
    result: List[Competitor] = quick_sort(inp_arr, n)
    print(*result, sep='\n')


if __name__ == '__main__':
    main()
