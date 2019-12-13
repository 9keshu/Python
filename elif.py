import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'My reply is no'
    else:
        return 'Very doubtful'

for fortune in range(6):
    fortune = getAnswer(random.randint(1,4))
    print(fortune + '.')
