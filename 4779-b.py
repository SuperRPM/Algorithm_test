import sys
input = sys.stdin.readline



def solution(text):
    length = len(text)
    if length < 3:
        result.append(text)
        return
    else:
        solution(text[:length // 3])
        result.append(' ' * (length // 3))
        solution(text[(length // 3) * 2:])
# '--    ----          ---------'
while True:
    try:
        N = int(input())
        total_length = 3 ** N
        first_text: str = '-' * total_length
        result = []
        solution(first_text)
        print(''.join(result))
    except:
        break

# str 과 list중 하나만 써도 될거같고 그렇게 해야 시간이나 메모리 절약 가능할듯
# list의 경우 총 길이가 정해져 있으니까 tuple로 생성해줘도 괜찮을듯