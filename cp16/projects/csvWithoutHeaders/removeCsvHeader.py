#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current

# working directory.

import csv, os

from pathlib import Path

path = os.path.dirname(os.path.realpath(__file__))
folderCsvNoHeaders = os.path.join(path, 'headerRemoved')
os.makedirs(folderCsvNoHeaders, exist_ok=True)

# Loop through every file in the current working directory.
folderCsvHeaders = os.path.join(path, 'csvsWithHeaders')
for csvFilename in os.listdir(folderCsvHeaders):
    if not csvFilename.endswith('.csv'):
        continue    # skip non-csv files
    print('Removing header from ' + csvFilename + '...')

    file = open(os.path.join(folderCsvHeaders,csvFilename))
    reader = csv.reader(file)
    dataList = list(reader)

    outputFile = open(os.path.join(folderCsvNoHeaders,csvFilename), 'w', newline='')
    writer = csv.writer(outputFile)

    try:
        # skip header line
        for row in dataList[1:]:
            writer.writerow(row)
    except:
        print("Error writing. Skipping file.")
