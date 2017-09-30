#！ python3
import re,pyperclip

# 贪婪
pt = re.compile(r'(edi){2,4}')
match = pt.search('ediediediediediedi')
print(match.group())

# 非贪婪
pt2 = re.compile(r'(edi){2,4}?')
match2 = pt2.search('ediediediediediedi')
print(match2.group())
print(pt.findall('ediediediediediedi'))

"""
主办单位：中国田径协会、江苏省体育局
承办单位：苏州工业园区管理委员会、苏州市体育局、苏州汇创体育文化发展有限公司
咨询电话：0512-62600818
咨询邮箱：marathon@huisports.com
备案信息：苏ICP备10022837号-1
"""

phoneRegex = re.compile(r'''(
    (\d{4}|\(\d{4}\))          #区号
    (\s|-|\.)?                   #分隔符
    (\d{8})                      #前3位数字
    (\s|-|\.)?                    #分隔符
    (\d{4})?                      #后4位数字
    (\s*(ext|x|ext.)\s*(\d{2,5))? #分机
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           #用户名
    @
    [a-zA-Z0-9]+                #域名
    (\.[a-zA-Z]{2,4})           #.加上后缀
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phonenum = '-'.join([groups[1],groups[3]])
    matches.append(phonenum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')