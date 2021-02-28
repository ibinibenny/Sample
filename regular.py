

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
