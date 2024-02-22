# import re
# s="good morning"
# match=re.search(r'good',s)
# #print (match.start())
# #print (match.end()
# string="RegEx is a special sequence of characters that uses a search pattern to find a string or set of strings"
# pattern="[a-r]"
# result=re.findall(pattern,string)
# print(result)
# s=re.split("\s",string)
# print(s)
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)