import random
def collatz(number):
    if(number%2):
        return (number//2)
    else:
        return (3*number +1)

for num in range(10):
    num = collatz(random.randint(1,10))
    print(num)
