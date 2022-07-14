# In the previous exercise we saved information about famous scientists’ names and birthdays to disk. 
# In this exercise, load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.

import json
from datetime import datetime
from collections import Counter

filename = 'birthdays.json'
birth_months = {'January': 0,'February': 0,'March': 0,'April': 0,'May': 0,'June': 0,'July': 0,'August': 0,'September': 0,'October': 0,'November': 0,'December': 0}

with open(filename, 'r') as f:
    data = json.load(f)

for entry in data:
    bday = data[entry]
    birthmonth = datetime.strptime(bday, '%m/%d/%Y').strftime('%B')
    birth_months[birthmonth] += 1

for month in birth_months:
    num = Counter(birth_months)
    if int(birth_months[month]) > 0:
        print('There are {} entry(s) with birthdates in '.format(num[month])+month+'.')