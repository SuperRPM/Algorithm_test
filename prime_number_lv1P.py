from itertools import combinations
def solution(nums):
    answer = 0
    list_length = len(nums)
    n_list = list(sum(i) for i in combinations(nums, 3))
    for _ in n_list:
        checking_num = _
        check = True
        for _ in range(2, checking_num):
            if checking_num % _ == 0:
                check = False
        if check == True:
            answer += 1
    return answer


nums = [1, 2, 7, 6, 4]


print(list(sum(i) for i in combinations(nums,3)))