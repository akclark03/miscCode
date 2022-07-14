# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in!

from bokeh.plotting import figure, show, output_file
import json
from datetime import datetime

filename = 'birthdays.json'
birth_months = {'January': 0,'February': 0,'March': 0,'April': 0,'May': 0,'June': 0,'July': 0,'August': 0,'September': 0,'October': 0,'November': 0,'December': 0}

with open(filename, 'r') as f:
    data = json.load(f)

for entry in data:
    bday = data[entry]
    birthmonth = datetime.strptime(bday, '%m/%d/%Y').strftime('%B')
    birth_months[birthmonth] += 1

output_file('plot.html')

x_label = [i for i in birth_months if birth_months[i] != 0]
x = [i for i in x_label]
y = [birth_months[i] for i in x]

p = figure(x_range=x_label)
p.vbar(x=x, top=y, width=0.5)

show(p)