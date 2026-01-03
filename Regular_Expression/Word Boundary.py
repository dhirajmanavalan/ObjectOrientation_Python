"""i want to match abc string"""

# import re

# txt = """abcpqrstuvwxyz

# dsjdjhabc
# hjdsjabc
# abc"""

# regex = r"\babc"
# l = re.findall(regex, txt)
# print(l)
# print("number of occurences: ", len(l))


# import re

# txt = """abcpqrstuvwxyz

# dsjdjhabc
# hjdsjabcdff
# abc"""

# regex = r"abc\b"
# l = re.findall(regex, txt)
# print(l)
# print("number of occurences: ", len(l))

# import re

# txt = """abcpqrstuvwxyz

# dsjdjhabc
# hjdsjabc
# abc"""

# regex = r"\babc\b"
# l = re.findall(regex, txt)
# print(l)
# print("number of occurences: ", len(l))


# import re

# txt = """abcpqrstuvwxyz

# dsjdjhabc
# hjdsjabc
# kdsjabcdkj"""

# regex = r"\Babc\B"
# l = re.findall(regex, txt)
# print(l)
# print("number of occurences: ", len(l))


"""practise first word"""

# import re

# txt = "python is not java"
# regex = r"^[a-zA-Z]+"
# l = re.findall(regex, txt)
# print(l)


"""practise last word"""

# import re

# txt = "python is not java"
# regex = r"[a-zA-Z]+$"
# l = re.findall(regex, txt)
# print(l)

"""I want to match exact 4 characters"""
# import re

# txt = "python is best compare to C"
# regex = r'\b[a-zA-Z]{4}\b'
# match = re.search(regex,txt)
# print(match.group())

"""Email address is valid or not valid"""

# import re

# txt = '''
# kumardhiraj77@gmail.com
# dhir@gmail.com
# dhi@@gma.co
# dhi^@gmail.com
# dhi_kumar@gmail.com
# dhiru-@gmail.com
# '''

# regex = r"[a-zA-Z0-9_\-$]+@gmail.com"

# match = re.findall(regex,txt)
# print(match)

"""Email address ".com , .yahoo, ..." is valid or not valid"""

# import re

# txt = """
# kumardhiraj77@gmail.com
# dhir@gmail.com
# dhi@@gma.co
# dhi^@gmail.com
# dhi_kumar@gmail.com
# dhiru-@gmail.com
# dhi@yahoo.com
# """

# regex = r"[a-zA-Z0-9_\-$]+@[a-zA-Z]+.com"

# match = re.findall(regex, txt)
# print(match)

"""create separate groups-- it gives single object"""

# import re

# txt = """
# kumardhiraj77@gmail.com
# dhir@gmail.com
# dhi@@gma.co
# dhi^@gmail.com
# dhi_kumar@gmail.com
# dhiru-@gmail.com
# dhi@yahoo.com
# """

# regex = r"([a-zA-Z0-9_\-$]+)@([a-zA-Z]+.com)"

# match = re.search(regex, txt)
# print(match.group(0))
# print(match.group(1))
# print(match.group(2))


"""create separate groups-- it give every objectss"""

# import re

# txt = """
# kumardhiraj77@gmail.com
# dhir@gmail.com
# dhi@@gma.co
# dhi^@gmail.com
# dhi_kumar@gmail.com
# dhiru-@gmail.com
# dhi@yahoo.com
# """

# regex = r"([a-zA-Z0-9_\-$]+)@([a-zA-Z]+.com)"

# itr = re.finditer(regex, txt)

# for m in itr:
#     print(m.group(0))
#     print(m.group(1))
#     print(m.group(2))

"""i wants to change domain name"""

# import re

# txt = """
# kumardhiraj77@gmail.com
# dhir@gmail.com
# dhi@@gma.co
# dhi^@gmail.com
# dhi_kumar@gmail.com
# dhiru-@gmail.com
# dhi@yahoo.com
# """

# regex = r"@[a-zA-Z]+.com"

# s = re.sub(regex,"@rooman.com",txt)
# print(s)

"""i wants to change domain name using subn"""

# import re

# txt = """
# kumardhiraj77@gmail.com
# dhir@gmail.com
# dhi@@gma.co
# dhi^@gmail.com
# dhi_kumar@gmail.com
# dhiru-@gmail.com
# dhi@yahoo.com
# """

# regex = r"@[a-zA-Z]+.com"

# s = re.subn(regex, "@rooman.com", txt)
# print(s)


"""i want to separate month year date"""

import re

txt = "1992/02/22"

s = re.split(r"[/:-]",txt)
print(s)
