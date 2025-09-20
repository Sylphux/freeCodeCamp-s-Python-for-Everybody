
try :
    hours = float(input('Enter hours : '))
    rate = float(input('Enter rate : '))
except :
    print('Please input valid numbers')
    quit()
overtime = 0
if hours > 40 :
    overtime = hours - 40
overtime = overtime * rate * 1.5 
print('Your pay is : ' + str(hours * rate + overtime))
