birthdays = {'Alice':'Arp 1',
            'Bob': 'Dec 12',
            'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of  ' + name)
    else:
        print('I do not have the information for ' + name)
        print('What\'s your Birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')

        
