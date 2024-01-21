hrs = input('Enter hour: ')
rate = input('Enter rate: ')

fhrs = float(hrs)
frate = float(rate)

if fhrs > 40:
    reg = 40 * frate
    otp = (fhrs - 40) * (frate * 1.5)
    print('Regular pay:', reg, 'Overtime:', otp)
    pay = (reg + otp)
    print('Pay:', pay)
else:
    pay = fhrs * frate
    print('Pay:', pay)

