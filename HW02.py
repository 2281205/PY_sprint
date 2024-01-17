operatorArr = ['+', '-', '*', '/']
def numCheck(num):
    try: return int(num)
    except ValueError: print('wrong number! Set number = 0')
    return int(0)
def switch(num01, num02, operator):
    if operator == "/" and num02 == 0: return print('Wrong! Division by zero is impossible \n')
    elif operator == "+": return num01+num02
    elif operator == "-": return num01-num02
    elif operator == "*": return num01*num02
    elif operator == "/": return num01/num02

print('Hi! calc')
num01 = numCheck(input('input first number:'))
operator = input('input operator:')
if operator not in operatorArr:
    print('wrong operator! Set +')
    operator = '+'
num02 = numCheck(input('input second number:'))
print('Your result:', num01, operator, num02, "=", switch(num01, num02, operator))
