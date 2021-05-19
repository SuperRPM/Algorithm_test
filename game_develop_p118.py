n, m = map(int, input().split())
x, y, direction = map(int, input().split())
total_map = [[0] * m for _ in range(n)]

# create a map
for i in range(len(total_map)):
    total_map[i] = list(map(int, input().split()))

# 동서 남북 설정
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# turn left
def turn_left():
    global direction
    if direction == 0:
        direction = 3
    elif direction == 3:
        direction -= 1
    elif direction == 2:
        direction -= 1
    elif direction == 1:
        direction -= 1

# 최초 시작위치 방문으로 카운쪽
total_map[x][y] = 1
count = 1
precount = 1

# 방문 시작
while True:
    if direction == 0 and total_map[x - 1][y] == 0:
        x -= 1
        total_map[x][y] = 1
        count += 1
        print("north")
    elif direction == 3 and total_map[x][y - 1] == 0:
        y -= 1
        total_map[x][y] = 1
        count += 1
        print("west")
    elif direction == 2 and total_map[x + 1][y] == 0:
        x += 1
        total_map[x][y] = 1
        count += 1
        print("south")
    elif direction == 1 and total_map[x][y + 1] == 0:
        y += 1
        total_map[x][y] = 1
        count += 1
        print("east")
    else:
        if total_map[x - 1][y] == 1 and total_map[x][y - 1] == 1 and total_map[x + 1][y] == 1 and total_map[x][y + 1] == 1:
            break
        else:
            turn_left()

print(count)