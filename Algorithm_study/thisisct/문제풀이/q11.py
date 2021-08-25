# Dummy
n = int(input())
board = [[[0] * n] * n]
print(board)
k = int(input())
apple = []

for _ in range(k):
    apple_loc_x, apple_loc_y = map(int, input().split())
    apple.append((apple_loc_x, apple_loc_y))

print(apple)
change_cnt = int(input())
change_info = []

for _ in range(change_cnt):
    sec, direction = map(str, input().split())
    change_info.append([int(sec), direction])

board[0][0] = 1

for a, b in apple:
    board[a][b] = "apple"

print(board)


def solution():

    answer = True
    return answer