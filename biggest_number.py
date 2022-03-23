from itertools import permutations
from time import time

def solution(numbers):
    string_list = list(map(str, numbers))
    string_list = sorted(string_list, key=lambda x: (x[0], x[1:]), reverse=True)

    while string_list[0] == '0':
        if len(string_list) > 1:
            string_list = string_list[1:]
        else:
            return string_list[0]
    print(string_list)
    return ''.join(string_list)#41441 41441

numbers = [3, 30, 34, 5, 9]	#"9534330"
start = time()
print(solution(numbers))
end = time()
print((end - start)*100000)
numbers = [412, 41]#"41412"
start = time()
print(solution(numbers))
end = time()
print((end - start)*100000)