s = input()
cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
for i in cro_alpha:
    s = s.replace(i, '@')
print(len(s))