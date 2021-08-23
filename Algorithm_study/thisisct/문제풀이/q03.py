data = input()
first = data[0]
count = 0

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i] == first:
            count += 1

print(count)

