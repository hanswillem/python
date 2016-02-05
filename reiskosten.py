import csv
from datetime import date
import calendar

f = open('transacties 01.csv', 'rw')
count = 0
total = 0
validTransits = []
invalidTransits = []

stops = ['Zuiderzeeweg', 'Centraal Station', 'Amsterdam Centraal', 'Ede-Wageningen']

for row in f:
    if count > 0:
        currentTotal = total

        #get date and day of the week
        dateString = row.split(';')[0]
        dateString = dateString[1:-1]
        year = int(dateString[-4:])
        month = int(dateString[3:5])
        day = int(dateString[0:2])
        theDate = date(year, month, day)
        dayOfTheWeek = calendar.day_name[theDate.weekday()]

        #get to and from stops
        fromStop = row.split(';')[2]
        fromStop = fromStop[1:-1]
        toStop = row.split(';')[4]
        toStop = toStop[1:-1]

        #get cost
        costString = row.split(';')[5]
        costString = costString[1:-1]
        cost = float (costString.split(',')[0] + '.' + costString.split(',')[1])

        #find home-work transits
        if dayOfTheWeek != 'Saturday' and dayOfTheWeek != 'Sunday':
            if fromStop in stops and toStop in stops:
                total += cost
                validTransits.append(dayOfTheWeek + ' ' + dateString +': ' + fromStop + ' - ' + toStop + ': ' + 'EUR ' + costString)

        if currentTotal == total:
            invalidTransits.append(dayOfTheWeek + ' ' + dateString +': ' + fromStop + ' - ' + toStop + ': ' + 'EUR ' + costString)

    count += 1


print '-----valid:-----'


for i in validTransits:
    print i

print '-----invalid:-----'

for i in invalidTransits:
    print i

print ''
print 'total: ' + str(total)

f.close()
