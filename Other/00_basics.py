def cringeprint(s) :
    i = 1
    for n in s :
        print(n, end = '')
        for x in range (0, i) :
            print(' ', end = '')
        i = i + 1
    print('?')

print('Hello world. Welcome to my first Py program.')
print('Please, give me your age')

age = input('age : ')

try :
    age = int(age)
except :
    print('Error : not a number. Please try harder.')
    quit()

name = input('name : ')

print('first letter of your name is ', name[0], 'but your name is', len(name), 'letters long')
print('Lets just be sure...')
for n in name :
    print(n)
print('....')

if age < 18 and age > -1 :
    print('This program is unallowed for underaged bros.')
    print('do you understand,')
    cringeprint(name)
    quit()
elif age > 100 :
    print('wow. Impressive.')
elif age > 18 and age < 101 :
    print('Okay. Your age seems fine and legit.')
else :
    print('This is supposed to be sus. What are you ? Monster.')

print('in 100 years, you will be ' + str(age + 100))

birth = input('what is your date of birth : ')

try :
    birth = int(birth)
except :
    print('You typed ', end = '')
    cringeprint(birth)
    print('Not a number. Please try harder.')
    quit()

print('So... The current year should be ' + str(birth + age + 1))