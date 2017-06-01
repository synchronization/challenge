import csv
import numpy as np

with open('Challenge.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')

    first = next(csvreader, None)
    dates = first[10:40]
#    print dates

    names = ['date'] # the d3 visualization needs this
    all_acc_logs = []

    for inputrow in csvreader:
        name = inputrow[1]
        name = name.replace('.', '')
        names.append(name)

        logs = inputrow[41:]

        acc_logs = []
        acc_log = 0.0
        for i in range(len(logs)):
            if logs[i] == '':
                appendee = None
            else:
                acc_log = acc_log + float(logs[i])
#                appendee = acc_log
                appendee = np.exp(1.0 * acc_log / (i+1)) * 10000

#            print '----'
#            print 'i: ', i
#            print 'appendee: ', appendee

            acc_logs.append(appendee)

        all_acc_logs.append(acc_logs)

    all_acc_logs_transpose = zip(*all_acc_logs)

    with open('acc-data.tsv', 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='\t',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csvwriter.writerow(names)

        for i in range(len(dates)):
            writing_row = [dates[i]]
            writing_row = writing_row + list(all_acc_logs_transpose[i])

            csvwriter.writerow(writing_row)
