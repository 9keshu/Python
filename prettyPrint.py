import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {} # empty dictionary

for characters in message:
    count.setdefault(characters,0)
    count[characters] = count[characters]+1

pprint.pprint(count)
x=pprint.pformat(count)
print(x)
