import csv

from utils import utils


# this is where i test stuff
# im lonely and i miss serena
# coding the longing away

file = "expressions.csv"
e = "\p{Greek}"
e_list = ["\p{Greek}", "\p{Cyrillic}", "\p{Korean}"]

# print(utils.expression_already_in_file("\p{Greek}", file))

# print(utils.read_from_csv(file))
# for i in e_list:
#    print(utils.expression_already_in_file(i, file))

#print(utils.write_to_csv(e, file))

if utils.expression_already_in_file(e, file):
    expressions = utils.read_from_csv(file)
    expressions.remove([e])
    print(expressions)

    with open(file, "w") as csv_file:
        csv_data = csv.writer(csv_file)
        csv_data.writerows([expressions])