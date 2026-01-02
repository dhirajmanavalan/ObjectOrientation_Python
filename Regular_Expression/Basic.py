"""How to use regular expression"""

# import re
# Text = 'Python is super easy'
# regex = r'Python'
# match = re.match(regex , Text)
# print(match)

# # start,end = match.span()
# # print(Text[start:end:])

# print(Text[match.start():match.end():])

"""search function difference btwn match function"""

import re

Text = "Python is super easy"
regex = r"super"
match = re.search(regex, Text)
print(Text[match.start() : match.end() :])
