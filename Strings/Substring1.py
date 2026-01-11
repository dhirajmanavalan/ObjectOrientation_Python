'''Find substring for a string'''

# s = input("Enter a string:\n")

# for i in range(0,len(s)-4):
#     print(s[i+1:i+5])

'''print all character from string exclude firstletter and last letter'''

# s = input("Enter string:\n")

# print(s[1:len(s)-1])

'''print all character from string exclude firstletter and last letter'''

# s = input("Enter string:\n")

# print(s[len(s)-2:0:-1])

# # x = s[::-1]
# # print(x[1:len(x)-1])

'''Check Palindrome string or not'''

s = input("Enter String: ")
x = s[::-1]

if s==x:
    print(s," Palindrome ",x)
else:
    print(s, "Not Palindrome ",x)

