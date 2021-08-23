data = "K1KA5CB7"

result = []
value = 0
number = False

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        number = True
        value += int(x)

result.sort()
if number is True:
    result.append(str(value))

print(''.join(result))
