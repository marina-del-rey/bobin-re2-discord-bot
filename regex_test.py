import re2 as re

txt = "Χαίρετε"
regex = re.search(r"\p{Greek}", txt)

print(regex)
