s = int(input())
answer = 0
count = 0
while True:
    count += 1
    answer += count
    if answer == s:
        print(count)
        break
    elif answer > s:
        print(count - 1)
        break
