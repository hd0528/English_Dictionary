#English Dictonary

import json
import difflib 
from difflib import get_close_matches

data = json.load(open("Application_1/data.json"))

user_input = input("Enter Word : ")

similirity = get_close_matches(user_input, data.keys())

def meaning(inp):

    inp = inp.lower()

    if inp in data:
        return data[inp]
    elif inp.title() in data:
        return data[inp.title()]
    elif inp.upper() in data:
        return data[inp.upper()]
    elif len(similirity) > 0:
        yn = input(f"Did you mean {(similirity)[0]} instead? Press Y for YES and N for NO : ").upper()
        if yn == 'Y':
            return data[(similirity)[0]]
        elif yn == 'N':
            return "The Word Dosen't Exists, Please Double Check!!"
        else:
            return "Invalid Input!!"
    else:
        return "The Word Dosen't Exist, Please Double Check!!"

output = meaning(user_input)

if type(output) == list:
    for items in output:
        print(items)
else:
    print(output)
    







