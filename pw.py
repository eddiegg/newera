#! python3
# An insecure psw locker program

PASSWORD = {'email': 'asdfasdfasg7102!@#',
            'blog': 'y^%$*&(jkljk123',
            'luggage': '$asdf*%'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print('Password for ' + account + ' is copied to clipboard.')
else:
    print('There is no account named ' + account)



