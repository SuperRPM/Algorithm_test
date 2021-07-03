def solution(board, moves):
    answer = 0
    basket = []

    # move to basket
    for move in moves:
        for floor in board:
            if floor[move - 1] != 0:
                basket.append(floor[move - 1])
                floor[move - 1] = 0
                break

    # pop it!      mutalbe immutable
    none_count = 0
    pre = -1
    while pre != len(basket):
        pre = len(basket)
        for i in range(len(basket) - 1):
            if basket[i] == basket[i + 1]:
                basket[i + 1] = None
                basket[i] = None
                answer += 2
                none_count += 2

        for i in range(none_count):
            basket.remove(None)
        none_count = 0

    return answer

print(solution(board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], moves=[1,5,3,5,1,2,1,4]))
