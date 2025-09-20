
def verify(src) :
    try:
        src = int(src)
        return True
    except:
        if src != "done" :
            print('Error : wrong input. Either type a number or type done.')
    return False

total = 0
i = 0
smallest_known = None
biggest_known = None

while True :
    src = input('Input numbers : ')
    if src == "done" :
        break
    if verify(src) :
        total = total + int(src)
        i = i + 1
        if smallest_known == None or smallest_known > int(src) :
            smallest_known = int(src)
        if biggest_known == None or biggest_known < int(src) :
            biggest_known = int(src)

if i == 0 :
    i = 1
    print('Nothing entered.')
else :
    print('\nTotal :', str(total), '\nIterations :', str(i), '\nAverage :', str(total / i)) #Exercice 1
    print('Smallest known :', str(smallest_known), '\nBiggest known :', str(biggest_known)) #Exercice 2