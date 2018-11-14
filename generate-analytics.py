import csv
import numpy as np
import requests
import sys

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
    str_values = inputrow[start_col:end_col+1]

    # remove possible comma in each number
    #"10,000.00".replace(",", "")

    acc_values = []
    acc_value = 0.0
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
#sheet_address = 'https://docs.google.com/spreadsheets/d/1nUWyMeji2DZr0TnIXPKlQGGJ-siBM9XaotDF1E_NBdE/export?format=csv'
# sheet_address = 'https://docs.google.com/spreadsheets/d/1M1ybDeETcjvLaXS9pFaa1swaQMoIXB9vupGhZ_0yV2c/export?format=csv'
sheet_address = 'https://docs.google.com/spreadsheets/d/1FPtoRu6FJS8EGDueLNkLOZzDEDLl1NWOJWpXMjsDDOc/export?format=csv'

response = requests.get(sheet_address)
#print '-RDF95134- response: ', response
#print '-RDF95208- response.status_code: ', response.status_code
#print '-RDT41731- response.text: ', response.text
#print '-RDT112937- response.content: ', response.content

if (response.status_code != 200):
    print 'Wrong status code in reading the spreadsheet: ', response.status_code
    sys.exit()
    
with open('Challenge.csv', 'w') as csvfile:
    csvfile.write(response.content)

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
