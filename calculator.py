def add(x,y):
    return x+y
    
def subtract(x,y):
    return x-y
    
def multiply(x,y):
    return x*y
    
def divide(x,y):
    return x/y
    
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
            print(num1, '+', num2, '=', add(num1, num2))
            
        elif choice == '-':
            print(num1, '-', num2, '=', subtract(num1, num2))
            
        elif choice == '*':
            print(num1, '*', num2, '=', multiply(num1, num2))
            
        elif choice == '/':
            print(num1, '/', num2, '=', divide(num1, num2))
            
        elif choice == '^':
            print(num1, '^', num2, '=', pow(num1, num2))
            
        next_calculation = input('Do another one? [y/n]: ')
        if next_calculation == 'n':
            break
        
    else:
        print('invalid')
