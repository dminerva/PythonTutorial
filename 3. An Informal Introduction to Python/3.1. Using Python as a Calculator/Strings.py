print('spam eggs')

print('C:\some\name')  # here \n means newline!

print(r'C:\some\name')  # note the r before the quote

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")    #String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''.

print(3 * 'un' + 'ium') # 3 times 'un', followed by 'ium'

word = 'Python'
print(word[0])  # character in position 0
print(word[5])  # character in position 5
print(word[-1])  # last characte
print(word[-2])  # second-last character
print(word[0:2])  # characters from position 0 (included) to 2 (excluded)