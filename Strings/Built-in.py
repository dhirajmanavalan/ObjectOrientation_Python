# string = ['python' , 'java' , 'c++' , 'django']
# # s = ""

# # for i in string:
# #     s = s+i+" "

# s = "".join(string)
# print(s)

# import re

'''Program to count number of lowercase, uppercase , specialcharacter, numbers'''
st = "JaVaIsAlaNGuagE@098!"

# d_count = 0
# l_count = 0
# c_count = 0
# s_count = 0
# for i in st:
#     if re.match(r"\d",i):
#         d_count += 1
    
#     elif re.match(r"[a-z]",i):
#         l_count += 1
    
#     elif re.match(r"[A-Z]", i):
#         c_count += 1
    
#     else:
#         s_count +=1
        

# print(d_count)
# print(l_count)
# print(c_count)
# print(s_count)


# s = "i love python"

# print(s.title())

# print(s.capitalize())

s = "Dhiraj 123 @ Pyhton"

table = s.maketrans("aeiou","AEIOU","123@")
print(type(table))
print(table)

str_table = s.translate(table)
print(str_table)