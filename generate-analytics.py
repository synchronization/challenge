import csv
import numpy as np
import requests
import sys

start_col = 14 # counting from 0
end_col = 34 # inclusive, counting from 0

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
    str_values = inputrow[start_col:end_col+1]

    # remove possible comma in each number
    #"10,000.00".replace(",", "")

    acc_values = []
    # acc_value = 0.0
    for i in range(len(str_values)):
        if str_values[i] == '':
            appendee = None
        else:
            # convert the strings to float
            values = [float(x.replace(",", "")) for x in str_values[0:i+1]]
            # use the following line for log
            # appendee = np.exp(1.0 * find_average(values, 3)) * 10000.0
            # use the following line for linear
            appendee = find_average(values, 3)

        acc_values.append(appendee)

    return acc_values

# ----------------------------

# download the Google spreadsheet
# sheet_address = 'https://docs.google.com/spreadsheets/d/1U0q9MlNydskH0tPIH5nEwCdmB0ahvhm143zdUIN3H1s/export?format=csv'
sheet_address = 'https://docs.google.com/spreadsheets/d/1liyW0ymb1mk3JWfoJJLi8GcecD4G9NWWUUfAm5fBx4g/export?format=csv'

response = requests.get(sheet_address)

if (response.status_code != 200):
    print('Wrong status code in reading the spreadsheet: ', response.status_code)
    sys.exit()
    
with open('Challenge.csv', 'wb') as csvfile:
    csvfile.write(response.content)

# with open('Challenge.csv', 'rb') as csvfile:
with open('Challenge.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')

    first = next(csvreader, None)
    dates = first[start_col:end_col+1]

    names = ['date'] # the d3 visualization needs this
    all_acc_values = []

    for inputrow in csvreader:
        person_acc_values = make_person_acc_values(inputrow)
        all_acc_values.append(person_acc_values)

    # all_acc_values_transpose = zip(*all_acc_values)
    all_acc_values_transpose = list(map(list, zip(*all_acc_values)))

    # with open('acc-data.tsv', 'wb') as csvfile:
    with open('acc-data.tsv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='\t',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(names)

        for i in range(len(dates)):
            writing_row = [dates[i]]
            writing_row = writing_row + list(all_acc_values_transpose[i])

            csvwriter.writerow(writing_row)
