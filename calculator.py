def add(x,y):
    return x+y
    
def subtract(x,y):
    return x-y
    
def multiply(x,y):
    return x*y
    
def divide(x,y):
    return x/y
    
print('What do you want to do?')
print(' ')
print('Addition (+)')
print('Subtraction (-)')
print('Multiplication (*)')
print('Division (/)')
print('Exponent (^)')

while True:
    choice=input('Choose [+,-,*,/,^]: ')
    
    if choice in('+','-','*','/','^'):
        num1 = float(input('First number: '))
        num2 = float(input('Second number: '))
        
        if choice == '+':
            print(num1, 'plus', num2, 'is', add(num1, num2))
            
        elif choice == '-':
            print(num1, 'subtracted by', num2, 'is', subtract(num1, num2))
            
        elif choice == '*':
            print(num1, 'multiplied by', num2, 'is', multiply(num1, num2))
            
        elif choice == '/':
            print(num1, 'divided by', num2, 'is', divide(num1, num2))
            
        elif choice == '^':
            print(num1, 'to the power of', num2, 'is', pow(num1, num2))

        next_calculation = input('Do another one? [y/n]: ')
        if next_calculation == 'n':
            break
        
    else:
        print('invalid')
