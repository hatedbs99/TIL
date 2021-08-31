a = "30+70-80-90+70-90-80+70"


a = a.split('-')
result = 0
for i in a[0].split('+'):
    result += int(i)

for i in a[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)
