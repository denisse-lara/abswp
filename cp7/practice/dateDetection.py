#! python3
# dateDetection.py - Reads a date in DD/MM/YYYY format and checks
# if it is valid.
# Usage: dateDetection.py <date>

import sys, re

from datetime import datetime as dt

if len(sys.argv) != 2:
    print("Usage: dateDetectionlpy <date>")
    sys.exit()

dateRegx = re.compile(r'(\d{2})/(\d{2})/(\d{4})')

inputDate = sys.argv[1]
m = dateRegx.search(inputDate)

if not m:
    print("Date doesn't match format DD/MM/YYYY")
    sys.exit()

try:
    if int(m.groups()[1]) > 12 or int(m.groups()[1]) < 0:
        raise ValueError("month must be between 01-12")

    date = dt.strptime(inputDate, "%d/%m/%Y")
except ValueError as err:
    print(err)
else:
    print("Valid date.")
