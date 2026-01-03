"""Approach 1"""

# import re

# txt = "8489403967 8484849"
# regex = r"[\d]{10}"
# l = re.search(regex, txt)
# print(l)

"""Approach 2"""

# import re

# txt = "8489403967 8484849"
# p = re.compile(r"[\d]{10}")
# l = p.search(txt)
# print(l)

"""check valid phone number and 6th digit should be 0 or 2 or 4 or 8 -- approach 1"""
# import re

# txt = """
# 8489403967
# 9443966107
# 9487122733
# 9042177033
# 94899762
# 92343478
# 9912311245
# 90182689100
# """

# regex = r"\b\d{5}[0248]\d{4}\b"
# l = re.findall(regex, txt)
# print(l)

"""check valid phone number and 6th digit should be 0 or 2 or 4 or 8 -- approach 2"""

import re

txt = ["9042100733", "9487122733", "9042177033", "9443966107", "8489403967"]

p = re.compile(r"\b\d{5}[123]\d{4}\b")
for i in txt:
    if p.search(i) != None:
        print(i, "valid")
    else:
        print(i, "not valid")
