from utils import utils

# this is where i test stuff
# im lonely and i miss serena
# coding the longing away

file = "expressions.csv"
e = "\p{Korean}"
e_list = ["\p{Greek}", "\p{Cyrillic}", "\p{Korean}"]

#print(utils.expression_already_in_file("\p{Greek}", file))

#print(utils.read_from_csv(file))
#for i in e_list:
#    print(utils.expression_already_in_file(i, file))

print(utils.write_to_csv(e, file))