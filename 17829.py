import sys
input = sys.stdin.readline

N = int(input())

beginning_matrix = [list(map(int, input().split())) for _ in range(N)]

def pick_up_the_kong(matrix):
    length = len(matrix)
    if len(matrix) == 1:
        print(matrix[0][0])
    else:
        after_matrix = [[] for _ in range(length // 2)]
        for row in range(0, length, 2):
            for col in range(0, length, 2):
                after_matrix[row//2].append(sorted([matrix[row][col], matrix[row][col+1], matrix[row+1][col], matrix[row+1][col+1]])[-2])
        pick_up_the_kong(after_matrix)

pick_up_the_kong(beginning_matrix)
