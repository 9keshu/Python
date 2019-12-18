import pyperclip
numbers = ''
for i in range(200):
    numbers = numbers + str(i) + '\n'

flag=pyperclip.copy(numbers)
var = pyperclip.paste()
print(var)

print(flag)
print('Done.')
