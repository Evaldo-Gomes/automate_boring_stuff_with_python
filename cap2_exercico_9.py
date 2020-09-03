import sys

span = ''

print('Type a number.')
span = input()

if span == '1':
    print('Hello')
elif span == '2':
    print('Howdy')
else:
    print('Greetings')
    sys.exit()
