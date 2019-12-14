#validateInput.py

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a correct number for your age')

while True:
    print('Enter a new passowrd(only letter and numbers)')
    password=input()
    if password.isalnum():
        break
    print('Password can only have numbers and letters')


          
