# import re
# def check(str,pattern):
#     if re.search(pattern,str):
#         print("valid string")
#     else:
#         print("invalid string")
# pattern=re.compile('^[1234]+$')
# check('2134',pattern)

# import re
# string="this is QuaStech !,1235"
# upper_case=re.findall(r"[A-Z]",string)
# Lower_case=re.findall(r"[a-z]",string)
# Number_case=re.findall(r"[0-9]",string)
# Special_case=re.findall(r"[!@#$%^&*]",string)
# print("The no. of uppercase charector is",len(upper_case))
# print("The no. of lowercase charector is",len(Lower_case))
# print("The no. of numbercase charector is",len(Number_case))
# print("The no. of symbolcase charector is",len(Special_case))

# import re
# txt="the search window"
# x=re.search("^the.*window$",txt)
# if x:
#     print("yes, match")
# else:
#     print("no match")

# import re
# txt="the rain is spain"
# x=re.findall("t",txt)
# print(x)

# import re
# txt="the dhoni is best"
# x=re.split("\s",txt,2)
# print(x)


# import re
# txt="the dhoni is best cricketer"
# x=re.sub("\s","2",txt)
# print(x)

# import re
# def extramax(input):
#     n=re.findall('\d+',input)
#     n=map(int,n)
#     print (max(n))
# if __name__=="__main__":
#     input='122ghnvcdertyhjmn6854712369854'

# import re
# def match(txt):
#     pattern='[A-Z]+[a-z]+$'
#     if re.search(pattern,txt):
#         return("yes")
#     else:
#         return ("no")
#
# print(match("Payal"))
# print(match("Geeks"))
