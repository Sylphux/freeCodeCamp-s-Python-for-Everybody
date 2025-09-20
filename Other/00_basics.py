print('Hello world. Welcome to my first Py program.')
print('Please, give me your age')

age = input('age :')

try :
    age = int(age)
except :
    print('Error : not a number. Please try harder.')
    quit()
if age < 18 and age > -1 :
    print('This program is unallowed for underaged bros.')
elif age > 100 :
    print('wow. Impressive.')
elif age > 18 and age < 101 :
    print('Okay. Your age seems fine and legit.')
else :
    print('This is supposed to be sus. What are you ???')

print('in 100 years, you will be ' + str(age + 100))


try :
    birth = int(input('what is your date of birth ? '))
except :
    print('Error : not a number. Please try harder.')
    quit()

print('so the current year should be ' + str(birth + age))