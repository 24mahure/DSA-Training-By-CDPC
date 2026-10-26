name = "prashant*is*a*good*programmer"

new = ''
val = ''

for i in name:
    if i != '*':
        new += i
    else:
        val += i

print(val + new)