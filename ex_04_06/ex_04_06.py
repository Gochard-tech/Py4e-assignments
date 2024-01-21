def computepay(hours, rate):
    if hours > 40:
        reg = 40 * frate
        otp = (hours - 40) * (rate * 1.5)
        #print('Regular pay:', reg, 'Overtime:', otp)
        pay = (reg + otp)
        #print('Pay:', pay)
    else:
        pay = hours * rate
        #print('Pay:', pay)
    return pay


hours = input('Enter hour: ')
rate = input('Enter rate: ')

fhrs = float(hours)
frate = float(rate)
xp = computepay(fhrs, frate)    

print('Pay',xp)

