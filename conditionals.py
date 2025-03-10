"""Starting with if, it works like this
   if <expr>:
        <statement>
    else: 
        <statement>"""


a = 4
b = 12

if a > b: 
    print('a is bigger than b')
else: 
    print('b is bigger than a')

#There is also elif but in my opinion would be better to use a switch maybe, there is no switch in Python, but there is a match

#other way of writting the if are like this:
c = 'Jhon'
d = 'Chad'
if c == 'Chad': print('hi, your name is' + c); print('how are you?')
else: print("I don't know you ")

#match statement, I think that is better when you have a lot of choices
today = 'monday'

def hello(day):
        match day:
            case 'monday':
                print("I hate monday's")
            case 'friday':
                print('time to sleep')

hello(today)

#Just trying match and other things

e = True
f = False

def checkLight(g):
        match g:
            case True:
                print('Light is on')
            case False:
                print('Light is off')

checkLight(e)
checkLight(f)


h = 5
"""
def checkNumber(number):
        match number:
            case number < 5:
                print('your number is < 5')
            case number == 5:
                print('your number is 5')
            case number > 5:
                print('your number is > 5')

checkNumber(a)
checkNumber(h)
"""
#Trying elif (in my opinion it would be better to use match)[I was wrong]

def ckNumber(number):
    if number > 5:
        print('your number is higher than 5')
    elif number < 5:
        print('your number is lower than 5')
    else:
        print('your number is 5')
ckNumber(b)
ckNumber(h)
#As I saw, match is just for patterns not for comparations like if so my code would not function

def checkNumber(number):
        match number:
            case _ if  number < 5:
                print('your number is < 5')
            case 5:
                print('your number is 5')
            case _ if number > 5:
                print('your number is > 5')

checkNumber(a)
checkNumber(h)


