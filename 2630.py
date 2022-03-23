import sys
input = sys.stdin.readline
import time

N = int(input())
paper = []

for _ in range(N):
    paper.append(list(map(int, input().split())))

negative = 0
zero = 0
positive = 0
def divide(matrix):
    n = len(matrix)
    one_third = n // 3
    two_third = one_third * 2
    NW = []
    North = []
    NE = []
    W = []
    Center = []
    E = []
    SW = []
    S = []
    SE = []
    for i in range(n):
        if i < one_third:
            NW.append(matrix[i][:one_third]) # NW
            North.append(matrix[i][one_third:two_third]) # North
            NE.append(matrix[i][two_third:])# NE
        elif i < two_third:
            W.append(matrix[i][:one_third]) # W
            Center.append(matrix[i][one_third:two_third]) # Center
            E.append(matrix[i][two_third:])# E
        else:
            SW.append(matrix[i][:one_third]) # SW
            S.append(matrix[i][one_third:two_third]) # S
            SE.append(matrix[i][two_third:])# SE

    return NW, North, NE, W, Center, E, SW, S, SE


def color_check(divided_paper):
    global negative, zero, positive
    mixed = False
    part_sum = 0
    for low in divided_paper:
        part_sum += sum(low)
        if 1 in low or -1 in low:
            mixed = True

    if part_sum == 0 and not mixed:
        zero += 1
    elif part_sum == len(divided_paper) ** 2:
        positive += 1
    elif part_sum == -(len(divided_paper) ** 2):
        negative += 1
    else:
        NW, North, NE, W, Center, E, SW, S, SE = divide(divided_paper)
        color_check(NW)
        color_check(North)
        color_check(NE)
        color_check(W)
        color_check(Center)
        color_check(E)
        color_check(SW)
        color_check(S)
        color_check(SE)


# start = time.time()
color_check(paper)
print(negative)
print(zero)
print(positive)
# end = time.time()
# print(end - start)