import csv

import re2 as re

#txt = "Χαίρετε"
#regex = re.search("\p{Greek}", txt)

#print(regex)

file = "expressions.csv"
msg = "a hi "

with open(file, 'r') as csv_file:
    csv_data = csv.reader(csv_file, delimiter="\n")
    expressions = list(csv_data)

print(expressions[0])


for exp in expressions:
    for i in exp:
        if re.search("\{}".format(i), msg):
            print("FUCK U EGIRL")
