message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    #if character not in count:
    #    count[character] = 1
    #else:
    count.setdefault(character,0)
    count[character] = count[character] + 1

print(count)
