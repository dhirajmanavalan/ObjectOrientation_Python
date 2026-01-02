"""meta character "." """

# import re

# text = "Python is super easy to learn."
# regex = r"."
# match = re.match(regex, text)
# print(match)

"""findall()"""

# import re

# text = "Python is super easy to learn."
# regex = r"."
# match = re.findall(regex, text)
# print(match)


"""meta character "\" """

# import re

# text = "Python is super easy. to learn."
# regex = r"\."
# l = re.findall(regex, text)
# print(l)


"""meta character "|" """

# import re

# text = "Python is super easy. to learn."
# regex = r"Python | super"
# l = re.findall(regex, text)
# print(l)


"""meta character "*" """

import re

# text = "A whole hole is not an wwwhole."
# regex = r"w*hole"
# l = re.findall(regex, text)
# print(l)


"""meta character "?" """

# import re

# text = "A whole hole is not an wwwhole."
# regex = r"w?hole"
# l = re.findall(regex, text)
# print(l)


"""meta character "+" """

import re

# text = "A whole hole is not an wwwhole."
# regex = r"w+hole"
# l = re.findall(regex, text)
# print(l)

"""Practise meta characters """
# import re

# text = "I know that no one is there in the school now."
# regex = r"k?now?"
# match = re.findall(regex, text)
# print(match)
# print("No of occurences:", len(match))

"""meta character "+" """
# import re
# txt = '''gogle
# google
# gooogle
# goooogle
# gooooogle
# goooooogle
# '''
# regex = r"go{2}gle"
# l = re.findall(regex,txt)
# print(l)
# print("number of occurences: ",len(l))

# import re
# txt = '''gogle
# google
# gooogle
# goooogle
# gooooogle
# goooooogle
# '''
# regex = r"go{2,4}gle"
# l = re.findall(regex,txt)
# print(l)
# print("number of occurences: ",len(l))

# import re

# txt = """gogle
# google
# gooogle
# goooogle
# gooooogle
# goooooogle
# """
# regex = r"go{,5}gle"
# l = re.findall(regex, txt)
# print(l)
# print("number of occurences: ", len(l))

"""meta character "^" """
# import re

# txt = "python is not come from a snake python"
# regex = r"^python"
# search = re.search(regex,txt)
# print(search)

"""meta character "$" """

# import re

# txt = "python is not come from a snake python"
# regex = r"python$"
# search = re.search(regex,txt)
# print(search)


"""meta character "[]" """

# import re

# txt = "python is not come from a snake python"
# regex = r"[aeiou]"
# search = re.findall(regex, txt)
# print(search)
# print("Number of occurence:", len(search))


"""meta character "[^]" """

# import re

# txt = "python is not come from a snake python"
# regex = r"[^aeiou]"
# l = re.findall(regex, txt)
# print(l)
# print("Number of occurence:", len(l))

"""meta character "[]" for alphabetics ,, alphanumeric """

# import re

# txt = "python is not come from a snake python: 1234567890"
# regex = r"[a-zA-Z0-9]"
# search = re.findall(regex, txt)
# print(search)
# print("Number of occurence:", len(search))


"""meta character "[]" for alphanumeric """

# import re

# txt = "python is not come from a snake python: 1234567890"
# regex = r"\w"
# search = re.findall(regex, txt)
# print(search)
# print("Number of occurence:", len(search))

"""practice for not alphanumeric"""


# import re

# txt = "python is not come from a snake python: 1234567890"
# regex = r"[^\w]"
# search = re.findall(regex, txt)
# print(search)
# print("Number of occurence:", len(search))


"""practice for vowels repeat"""

# import re

# txt = "if fOOt becomes feet tooth becomes teeth"
# regex = r"[aeiouAEIOU]{2    }"
# search = re.findall(regex, txt)
# print(search)
# print("Number of occurence:", len(search))



"""practice"""

import re

txt = "Only the weak wait for the week  to end"
regex = r"we[ea]k"
search = re.findall(regex, txt)
print(search)
print("Number of occurence:", len(search))
