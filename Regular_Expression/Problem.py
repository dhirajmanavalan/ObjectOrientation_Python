import re
text = '''

dhiraj@outlook.com 2003-09-02 male
dinesh@gmail.com 2003-09-02 male
monisha@yahoo.com 1987/06/28 female
abinaya@outlook.in 2004:15:19 female

'''

regex = r"([a-zA-Z0-9]+)@[a-zA-Z0-9]+\.[a-zA-Z]+ ([0-9]{4}[-/:][0-9]{2}[-/:][0-9]{2})"
match = re.finditer(regex,text)

for i in match:
    name = i.group(1)
    age = i.group(2)
    l = re.split(r"[:/-]",age)
    print(name, "age is : " , 2026-int(l[0]))