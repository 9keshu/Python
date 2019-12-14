#! /usr/bin/python3
#pw.py An insecure password locker program.
Passwords = {'email':'abc123','blog':'456kgf','movie':'123'}
import sys,pyperclip
if len(sys.argv)<2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1] #first command line arg is the account name

if account in Passwords:
    pyperclip.copy(Password[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
