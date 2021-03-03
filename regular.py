
re.search(pattern, string, flags=0)

    Scan through string looking for the first location where the regular expression pattern produces a match, and return a corresponding match object. 
Return None if no position in the string matches the pattern; note that this is different from finding a zero-length match at some point in the string.

re.match(pattern, string, flags=0)

    If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding match object. 
Return None if the string does not match the pattern; note that this is different from a zero-length match.

 re.findall(pattern, string, flags=0)

    Return all non-overlapping matches of pattern in string, as a list of strings. 
    The string is scanned left-to-right, and matches are returned in the order found. If one or more groups are present in the pattern, return a list of groups; this will be a list of tuples if the pattern has more than one group. 
  Empty matches are included in the result.


# import re 
  
# print(re.search(r"^x","xenon")) 
# print(re.search(r"s$","geeks"))



# Extract valid emails from a string


# # Raw text 
# text = "Done info@geeksforgks.com conva. eeksforgmai@rocks.xyz mauris. pre@rsos_tium.index at love@gfg.in" 
  
# #import regex module 
# import re 
  
# #finding all valid emails using regex 
# reg = re.findall(r"[A-Za-z0-9_%+-.]+"
#                  r"@[A-Za-z0-9.-]+"
#                  r"\.[A-Za-z]{2,5}",text) 
  
# #printing all the valid emails found 
# print(reg)




# import re

# pattern = '^a...s$'
# test_string = 'abyss'
# result = re.match(pattern, test_string)

# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")	
