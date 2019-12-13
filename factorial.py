
def factorial(number):
    fact =1
    i=1
    while(i<=number):
        fact=fact*i
        i+=1
        
    return fact

x= input()
ans=factorial(int(x))
print('Factorial of '+ x +' is : ' + str(ans) + '.')
