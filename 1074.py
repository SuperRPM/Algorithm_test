import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

result = 0
def zet(r, c, length, point):
    half = (2 ** length) // 2
    two_quad = 2 ** ((length - 1) * 2)
    if length == 1:
        if r == 0 and c == 0:
            print(point)
        if r == 0 and c == 1:
            print(point + 1)
        if r == 1 and c == 0:
            print(point + 2)
        if r == 1 and c == 1:
            print(point + 3)
        return
    # 1 - 4
    # if (r < half and c < half):
    #     pass
    # 2 - 4
    if (r < half and c >= half):
        c -= 2 ** (length - 1)
        point += two_quad
    # 3 - 4
    elif (r >= half and c < half):
        r -= 2 ** (length - 1)
        point += two_quad * 2
    # 4 - 4
    elif (r >= half and c >= half):
        c -= 2 ** (length - 1)
        r -= 2 ** (length - 1)
        point += two_quad * 3
    # print(r, c, length)
    zet(r, c, length - 1, point)

zet(r, c, N, 0)
