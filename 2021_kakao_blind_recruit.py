

# stage 1
def lower(new_id):
    new_id = new_id.lower()
    print("stage1" + new_id)
    return new_id
# stage 2
def char_delete(new_id):
    answer = ''
    special_word = ['.', '-', '_']
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    for _ in new_id:
        if _ in special_word or _ in alphabet or _ in numbers:
            answer += _
    print("stage2" + answer)
    return answer
# stage 3
def dot_delete(answer):
    while '..' in answer:
        answer = answer.replace("..", '.')
    print('stage3' + answer)
    return answer

# stage 4
def first_last_dot_delete(answer):
    if len(answer) > 0:
        if answer[0] == '.':
            answer = answer[1:]
    if len(answer) > 0:
        if answer[-1] == '.':
            answer = answer[:-1]
    print('stage4' + answer)
    return answer

# stage 5
def empty_space_add(answer):
    if answer == '':
        answer += 'a'
    print('stage5' + answer)
    return answer

# stage 6
def limit_15(answer):
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    answer = first_last_dot_delete(answer)
    print('stage6' + answer)
    return answer
# stage 7
def under_3_char_limit(answer):
    if len(answer) <= 2:
        for i in range(3 - len(answer)):
            answer += answer[-1]
    print('stage7' + answer)
    return answer

# soluton
def solution(new_id):
    answer = char_delete(lower(new_id))
    answer = dot_delete(answer)
    answer = first_last_dot_delete(answer)
    answer = empty_space_add(answer)
    answer = limit_15(answer)
    answer = under_3_char_limit(answer)
    return answer


print(solution(new_id="........................"))
print(solution(new_id="...!@BaT#*..y.abcdefghijklm"))