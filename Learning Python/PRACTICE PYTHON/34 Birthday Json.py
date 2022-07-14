# In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk,
# rather than having the dictionary defined in the program.

# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, 
# and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, 
# your JSON file should keep getting bigger and bigger.

import json
import time

filename = 'birthdays.json'

with open(filename, 'r') as f:
    data = json.load(f)
    
    print('Welcome to the Birthday dictionary. We have the birthdays of:\n')
    print("\n".join(data.keys()))
    time.sleep(3)
    while True:
        ask = input('\nWould you like to view or add an entry? ')
        
        if ask == 'view':
            time.sleep(1)
            name = input('What is the name of the entry? ')
            time.sleep(1)
            if name in data.keys():
                print(name + '\'s birthdate is ' + data[name])
                continue
            else:
                print('That name is not in the dictionary.')
                continue
        
        elif ask == 'add':
            time.sleep(1)
            name = input('What is the first and last name of your new entry? ')
            time.sleep(1)
            data[name] = input('What is the new entry\'s birthdate? (mm/dd/yyyy): ')
            time.sleep(1)
            print('Thank you!')
            time.sleep(2)
            continue

        elif ask.lower() == 'no' or ask.lower() == 'n':
            break

        else:
            time.sleep(1)
            print('Invalid response. Please type "view", "add", or "No"/"N".')
            time.sleep(2)
            continue

with open(filename, 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)