'''Group the string'''
import re
txt = '''
    dhiraj@gmail.com
    dhiraj@@gmail.com
    dhiraj_xyz@gmail.com
    dhi?>@gmail.com
    dhiraj-123@gmail.com
    dhiraj-1234@gmail.com
    dhiraj-12@info.in
    '''
regex = r"([a-zA-Z0-9_\-$]+)@([a-zA-Z]+.[a-zA-Z]+)"
match = re.finditer(regex,txt)

for i in match:
    print(i.group(0))
    print(i.group(1))
    print(i.group(2))

