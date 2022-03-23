def solution(answers):
    supo_one = [1,2,3,4,5]
    supo_two = [2,1,2,3,2,4,2,4,2,5]
    supo_three = [3,3,1,1,2,2,4,4,5,5]
    score_one = 0
    score_two = 0
    score_three = 0
    
    winner = {supo_one:1, 'supo_two':2, 'supo_three':3}
    
    for i in answers:
        if supo_one[i] == answers[i]:
            score_one += 1
    	if supo_two[i] == answers[i]:
            score_two += 1
        if supo_three[i] == answers[i]:
            score_three += 1
    
    answer = winner[supo_one]
    
    return answer