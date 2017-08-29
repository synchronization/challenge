import csv
import numpy as np

start_col = 10 # counting from 0
end_col = 40 # counting from 0

with open('Challenge.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')

    first = next(csvreader, None)
    print first
    print
    print first[0]
    print
    dates = first[start_col:end_col+1]
    print dates

    names = ['date'] # the d3 visualization needs this
    all_acc_logs = []

    for inputrow in csvreader:
        name = inputrow[1]
        name = name.replace('.', '')
        names.append(name)

        logs = inputrow[end_col+2:]

        acc_logs = []
        acc_log = 0.0
        for i in range(len(logs)):
            if logs[i] == '':
                appendee = None
                #break
            else:
                # convert the strings to float
                log_values = [float(x) for x in logs[0:i+1]]

                # for the first one we do not have minimum and so we treat it differently
                if i==0:
                    acc_log = acc_log + log_values[i]
                    count_total = 1
                else:
                    acc_log = sum(log_values) - min(log_values)
                    count_total = i

                # convert accumulated logs to average log steps
                appendee = np.exp(1.0 * acc_log / count_total) * 10000.0

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
