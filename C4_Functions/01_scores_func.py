
def getgrade(score) :
    if score > 1 or score < 0 :
        res = 'Wrong scope'
    elif score >= 0.9 :
        res ='A'
    elif score >= 0.8 :
        res ='B'
    elif score >= 0.7 :
        res ='C'
    elif score >= 0.6 :
        res = 'D'
    elif score < 0.6 :
        res = 'F'
    return res

score = input('Enter a score : ')
try :
    score = float(score)
except :
    print('Not a float.')
    quit()

print(getgrade(score))