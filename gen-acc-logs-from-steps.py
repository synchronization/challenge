import csv
#from itertools import izip

#a = izip(*csv.reader(open("Challenge6.csv", "rb")))
#csv.writer(open("Challenge6-pivot.csv", "wb")).writerows(a)

with open('Challenge6.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')

    first = next(csvreader, None)
    dates = first[9:39]
#    print dates

    names = ['date'] # the d3 visualization needs this
    all_acc_logs = []

    for inputrow in csvreader:
        name = inputrow[1]
        name = name.replace('.', '')
        names.append(name)

        logs = inputrow[40:]

#        print
#        print 'inputrow: ', inputrow
#        print 'len(inputrow): ', len(inputrow)
#        print 'logs: ', logs
#        print 'len(logs): ', len(logs)

        acc_logs = []
        acc_log = 0.0
        for i in range(len(logs)):
            if logs[i] == '':
                appendee = None
            else:
                acc_log = acc_log + float(logs[i])
                appendee = acc_log

            acc_logs.append(appendee)

        all_acc_logs.append(acc_logs)

    all_acc_logs_transpose = zip(*all_acc_logs)

    # remove the possible .s at the end of some names
#    for i in range(len(names)):
#        names[i] = names[i].replace('.', '')

#    print
#    print all_acc_logs_transpose

#    next(csvreader, None) # skip "No,1,2,3..."
#    names = next(csvreader, None)
#    names[0] = 'date' # replace Name with date, as needed by d3

#
#    print
#    print 'names: ', names
#
    with open('acc-data.tsv', 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='\t',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csvwriter.writerow(names)

#        print
#        print 'len(dates): ', len(dates)
#        print
#        print 'len(all_acc_logs_transpose): ', len(all_acc_logs_transpose)

        for i in range(len(dates)):
#            print 'type(list(all_acc_logs_transpose[i])): ', type(list(all_acc_logs_transpose[i]))

            writing_row = [dates[i]]
            writing_row = writing_row + list(all_acc_logs_transpose[i])
            #writing_row.append(list(all_acc_logs_transpose[i]))

            csvwriter.writerow(writing_row)
#
#        next(csvreader, None) # skip "Device,..."
#        next(csvreader, None) # skip "Notified,..."
#        next(csvreader, None) # skip "fee collected..."
#        next(csvreader, None) # skip "Days
#        next(csvreader, None) # skip Remaining",5,5,5,5,5,5,5,5,6,7,6,5,5,5,9,5,12,5,5,6,5,7,9,7
#        next(csvreader, None) # skip "Total
#        next(csvreader, None) # skip Steps
#        next(csvreader, None) # skip "Total
#        next(csvreader, None) # skip Score
#        next(csvreader, None) # skip Rank,19,11,21,9,14,20,2,13,7,18,22,3,15,1,24,4,16,23,6,5,12,10,17,8
#
#        for i in range (28):
#            next(csvreader, None) # skip others
#
#        for inputrow in csvreader:
#            print
#            print 'inputrow: ', inputrow
#
#            acc_log = 0.0
#            daily_logs = inputrow[1:-1]
##            print
##            print 'daily_logs: ', daily_logs
#            acc_logs = [inputrow[0]]
#            print
#            print 'acc_logs: ', acc_logs
#
#            for i in range(len(daily_logs)):
#                if (daily_logs[i] != ''):
#                    print '----'
#                    day_log = float(daily_logs[i])
#                    acc_log = acc_log + day_log
#
#                    print 'day_log: ', day_log
#                    print 'acc_log: ', acc_log
#
#                    acc_logs.append(acc_log)
#                else:
#                    acc_logs.append(None)
#
#            csvwriter.writerow(acc_logs)
