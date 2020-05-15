import re2 as re

txt = "Χαίρετε"
regex = re.search("\p{Greek}", txt)

print(regex)
