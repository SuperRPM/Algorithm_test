def solution(participant, completion):
    answer = ''
    set_participant = set(participant)
    set_completion = set(completion)
    who_fail = list(set_participant - set_completion)
    if len(who_fail) >= 1:
        answer = who_fail[0]
    else: # 동명이인 발생
        participant = sorted(participant)
        completion = sorted(completion)
        print(participant, '\n', completion)
        for i in range(len(completion)):
            if participant[i] != completion[i]:
                answer = participant[i]
                #return answer
        print(answer + "중간결과확인")
        if answer == '':
            answer = participant[-1]
    return answer
