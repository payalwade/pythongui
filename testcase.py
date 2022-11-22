# input_value='salman salim khan'
# record_name='mohd salmansalim khan'
# d1=input_value.split(" ")
# d2=record_name.split(" ")
# for item1 in d1:
#     for item2 in d2:
#         if item1 in item2 or item2 in item1 or item2==item1:
#             d2.remove(item2)
#             d2.append(item1)
# fullname=" ".join((map(str,d2)))
# print(fullname)
#
# Test Case 2:
# Input:
# name = "salmansalim khan"
# record_name = "mohd salman salim khan"
# Output:'mohd salmansalim khan'
#
# input_value="salmansalim khan"
# record_name="mohd salman salim khan"
# d1=input_value.split(" ")
# d2=record_name.split(" ")
# for item1 in d1:
#     for item2 in d2:
#         if item1 in item2 or item2 in item1 or item2==item1:
#             d2.remove(item2)
#             d2.append(item1)
# fullname=" ".join((map(str,d2)))
# print(fullname)
#
#
# import re
# address ="13/35 agedabout 60 years, residing at D.NO 59 Eswaran Koil St"
# pattern = "\d+(?=[\s]?year)"
# re.findall('\d.\s+',address)
#
# import re
# string ="13/35 agedabout 60 years, residing at D.NO 59 Eswaran Koil St"
# # regex = '\d+year'
# regex = (r'\(years\):\s\d{4}\s\(?Pyears>\d+\)')
#
# match = re.findall(regex, string)
# print(match)
#
#
# import re
#
# exampleString = '''13/35 agedabout 60 years, residing at D.NO 59 Eswaran Koil St '''
# num=[]
# for i in exampleString.split():
#     if i.isdigit():
#         num.append(i)
# print(num)
# # ages = re.findall(pattern="[0-9]+",string=exampleString)
# # print(ages)
# #
# import re
# regex = r"([a-zA-Z]+) (\d+)"
# match = re.search(regex, "13/35 agedabout 60 years, residing at D.NO 59 Eswaran Koil St")
# if match != None:
#     print("years: %s" % (match.group(2)))
# else:
#     print("The regex pattern does not match.")
# # # #
# import re
# regex = r"([a-zA-Z]+) (\d+)"
# match = re.search(regex, "16th street R.Kesavan age 46yrs, residing at D.NO 59Eswaran Koil St")
# if match != None:
#     print("%s" % (match.group(2)))
# else:
#     print("The regex pattern does not match.")
#
#
#
# import re
# regex = r"([a-zA-Z]+) (\d+)"
# match = re.search(regex, "Room no 43 R.Kesavan aged about 37years, residing at D.NO 59 Eswaran Koil St")
# if match != None:
#     print("year %s" % (match.group(2)))
# else:
#     print("The regex pattern does not match.")
#
#
# import re
# regex = r"([a-zA-Z]+) (\d+)"
# match = re.search(regex, "Door no 32 R.Kesavan 56yrs, residing at D.NO 59 Eswaran Koil St")
# if match != None:
#     print("%s" % (match.group(2)))
# else:
#     print("The regex pattern does not match.")
#
# import re
# regex = r"([a-zA-Z]+) (\d+)"
# match = re.search(regex, "12-4-67 , R.Kesavan aged about 61, residing at D.NO 59 Eswaran Koil St")
# if match != None:
#     print("year %s" % (match.group(2)))
# else:
#     print("The regex pattern does not match.")


# import re
# regex = r"([a-zA-Z]+) (\d+)"
# match = re.search(regex, "R.Kesavan age 63, residing at D.NO 59 Eswaran Koil St")
# if match != None:
#     print("%s" % (match.group(2)))
# else:
#     print("The regex pattern does not match.")

# import re
# regex = r"([a-zA-Z]+) (\d+)"
# match = re.search(regex, "R.Kesavan aged 9, residing at D.NO 59 Eswaran Koil St")
# if match != None:
#     print("year %s" % (match.group(2)))
# else:
#     print("The regex pattern does not match.")
#
# import editdistance
# l=editdistance.eval('salman khan', 'salmann khan')
# print(l)
#
# a = "salman khan"
# b = "salmann khan"
#
# ## The One-Liner
# ls = lambda a, b: len(b) if not a else len(a) if not b \
#          else min(ls(a[1:],b[1:]) + (a[0]!=b[0]),
#                   ls(a[1:],b) + 1,
#                   ls(a,b[1:]) + 1)
#
# ## The Result
# print(ls(a,b))
#
#
#
#
# name: “salman khan”
# document_name: “khan salmann”
# Output:
# [1,0]
#
# import editdistance
# l=editdistance.eval("salman khan", "khan salmann")
# print(l)
#
#

import editdistance
l=editdistance.distance("khan salman", "salim khan")
print(l)
#
#
#
# a = "khan salman"
# b = "salim khan"
#
# ## The One-Liner
# ls = lambda a, b: len(b) if not a else len(a) if not b \
#          else min(ls(a[1:],b[1:]) + (a[0]!=b[0]),
#                   ls(a[1:],b) + 1,
#                   ls(a,b[1:]) + 1)
#
# ## The Result
# print(ls(a,b))
#
#
#
# import re
# txt = "Gupta Company and 1 Other"
# x = re.findall("Gupta.*Company", txt)
# print(x)
#
# # name = "Gopoju-Upendar and 2 others"
# # Output:"gopoju upendar"
# import re
# txt = "Gupta Company and 2 Other"
# x = re.findall("Gupta.*Company", txt)
# print(x)
#
#
# import re
# txt="Chiluka Narsing Rao and another"
# x=re.findall("Chiluka.*Rao",txt)
# print(x)


# import re
# txt="HEMANTH ALIAS KENCHA ALIAS BOSS"
# x=re.findall("HEMANT.*HBOSS",txt)
# print(x)

# import re
# txt="Parvesh @ Pintu Ramesh Tandel and ors"
# x=re.findall("Pintu.*Tandel",txt)
# print(x)

# import re
# txt="Mr Yangmaso Khariwo and Ors"
# x=re.findall("Yangmaso.*Khariwo",txt)
# print(x)
