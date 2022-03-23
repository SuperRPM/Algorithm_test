def solution(new_id):
    answer = ''
    
    # stage 1
    new_id.lower()
    # stage 2
    special_word = ['.', '-', '_']
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for _ in new_id:
        if _ in special_word or _ in alphabet:
            answer += _
    # stage 3
    answer = answer.replace("...", '.')
    answer = answer.replace("..", '.')
    # stage 4
    print(answer + "stage5 answer state")
    if answer[0] == '.':
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    # stage 5
    print(answer + "stage5 answer state")
    if answer == '':
        answer += 'a'
    # stage 6
    if len(answer) >= 16:
        answer = answer[:16]
    # stage 7
    if len(answer) <= 2:
        for i in range(3 - len(answer)):
            answer += answer[-1]

    return answer

print(solution(new_id="...!@BaT#*..y.abcdefghijklm"))
print(solution(new_id="z-+.^."))
print(solution(new_id="=.="))
print(solution(new_id="123_.def"))
print(solution(new_id="abcdefghijklmn.p"))