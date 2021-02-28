
#  a string contains only a certain set of characters 

# import re
# def text_match(text):
#         patterns = 'ab*?'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
# print(text_match("ac"))
# print(text_match("abc"))
# print(text_match("abbc"))







#matches a string that has an a followed by zero or more b's

# import re
# def is_allowed_specific_char(string):
#     charRe = re.compile(r'[^a-zA-Z0-9.]')
#     string = charRe.search(string)
#     return not bool(string)

# print(is_allowed_specific_char("ABCDEFabcdef123450")) 
# print(is_allowed_specific_char("*&%@#!}{"))







# substrings within a string

# import re
# text = 'Python exercises, PHP exercises, C# exercises'
# pattern = 'exercises'
# for match in re.findall(pattern, text):
#     print('Found "%s"' % match)