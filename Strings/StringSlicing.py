# s = 'Dhiraj'
# print(s)
# print(s[0:5:])
# print(s[5:0:-1])
# print(s[-1:-7:-1])

# '''Reverse a string'''

# s = "Python"
# print(s[-1:-7:-1])

# s = "JAVA"
# print(s[::-1])


'''program to reverse the second half string'''

s = "Dhiraja"

print(s[:len(s)//2:] + s[len(s)-1:(len(s)//2)-1:-1])