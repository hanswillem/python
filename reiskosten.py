import csv
from datetime import date
import calendar

f = open('transacties 01.csv', 'rw')
count = 0
total = 0
transitRecorder = []

stops = ['Zuiderzeeweg', 'Centraal Station', 'Amsterdam Centraal', 'Ede-Wageningen']

for row in f:
    if count > 0:

        currentTotal = total

        dateString = row.split(';')[0]
        dateString = dateString[1:-1]
        year = int(dateString[-4:])
        month = int(dateString[3:5])
        day = int(dateString[0:2])
        theDate = date(year, month, day)
        dayOfTheWeek = calendar.day_name[theDate.weekday()]

        fromStop = row.split(';')[2]
        fromStop = fromStop[1:-1]

        toStop = row.split(';')[4]
        toStop = toStop[1:-1]

        costString = row.split(';')[5]

        costString = costString[1:-1]
        cost = float (costString.split(',')[0] + '.' + costString.split(',')[1])

        if dayOfTheWeek != 'Saturday' and dayOfTheWeek != 'Sunday':

            if fromStop == stops[2] and toStop == stops[3]:
                total += cost
                transitRecorder.append(row)
                print dayOfTheWeek + ' ' + dateString +': ' + fromStop + ' - ' + toStop + ': ' + 'EUR §' + costString
            if fromStop == stops[3] and toStop == stops[2]:
                total += cost
                transitRecorder.append(row)
                print dayOfTheWeek + ' ' + dateString +': ' + fromStop + ' - ' + toStop + ': ' + 'EUR §' + costString
            if fromStop == stops[0] and toStop == stops[1]:
                total += cost
                transitRecorder.append(row)
                print dayOfTheWeek + ' ' + dateString +': ' + fromStop + ' - ' + toStop + ': ' + 'EUR §' + costString
            if fromStop == stops[1] and toStop == stops[0]:
                total += cost
                transitRecorder.append(row)
                print dayOfTheWeek + ' ' + dateString +': ' + fromStop + ' - ' + toStop + ': ' + 'EUR §' + costString

    count += 1

print total

f.close()
