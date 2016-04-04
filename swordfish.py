while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the passwords (It is a fish.)')
    password = input()
    if password == 'fish':
        break
print('Access granted.')
