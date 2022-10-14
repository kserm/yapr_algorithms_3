def get_satisfied_kids(gr: list, cks: list) -> int:
    s = 0
    gr.sort()
    gr.reverse()
    cks.sort()
    for g in range(len(gr)):
        if cks:
            if gr[g] <= cks[-1]:
                s += 1
                cks.pop()
    return s
                

if __name__ == '__main__':
    kids = input()
    greed = [int(i) for i in input().split()]
    cookies_number = input()
    cookies = [int(i) for i in input().split()]
    print(get_satisfied_kids(greed, cookies))
