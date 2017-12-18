import csv
import numpy as np

start_col = 12 # counting from 0
end_col = 42 # counting from 0

# ----------------------------

def find_average(values, vacations):
    result = 0

    if len(values) > vacations:
        for i in range(vacations):
            values.remove(min(values))
    else:
        values = [max(values)]

    result = sum(values) / len(values)

    return result

# ----------------------------

def make_person_acc_values(inputrow):
    name = inputrow[1]
    name = name.replace('.', '')
    names.append(name)

    # read the values from the spreadsheet value (after the column for total)
    str_values = inputrow[end_col+2:]

    acc_values = []
    acc_value = 0.0
    for i in range(len(str_values)):
        if str_values[i] == '':
            appendee = None
        else:
            # convert the strings to float
            values = [float(x) for x in str_values[0:i+1]]
            appendee = np.exp(1.0 * find_average(values, 3)) * 10000.0

        acc_values.append(appendee)

    return acc_values

# ----------------------------

with open('Challenge.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')

    first = next(csvreader, None)
    dates = first[start_col:end_col+1]

    names = ['date'] # the d3 visualization needs this
    all_acc_values = []

    for inputrow in csvreader:
        person_acc_values = make_person_acc_values(inputrow)
        all_acc_values.append(person_acc_values)

    all_acc_values_transpose = zip(*all_acc_values)

    with open('acc-data.tsv', 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='\t',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(names)

        for i in range(len(dates)):
            writing_row = [dates[i]]
            writing_row = writing_row + list(all_acc_values_transpose[i])

            csvwriter.writerow(writing_row)
