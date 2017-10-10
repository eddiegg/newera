# coding:utf-8
import json

resp = '{"total":2,"num":{"N1":"1N"},"items":[{"reason":[{"R1":[{"R11":[]}],"R2":"2R"}],"date":"2016-07-05","out_reason":"未按规定期限公示年度报告被列入经营异常名录，现已补报未报年份的年度报告并公示","out_date":"2016-08-12","department":"北京市工商行政管理局"},{"reason":"未按规定期限公示年度报告","date":"2015-07-07","out_reason":"未按规定期限公示年度报告被列入经营异常名录，现已补报未报年份的年度报告并公示","out_date":"2016-08-12","department":"北京市工商行政管理局"}]}'

keys = []

def getListDictKeys(lst):
    if(len(lst)>0):
        if(isinstance(lst[0],dict)):
            getKeys(lst[0])

def getKeys(dic):
    for k,v in dic.items():
        keys.append(k)
        if(isinstance(v,dict)):
            keys.extend(v.keys())
        elif(isinstance(v, list)):
            getListDictKeys(v)
    return keys

resp1r = json.loads(resp)
print(resp1r)
extract_keys = getKeys(resp1r)
print(extract_keys)

try:
    assert(1 == 2)
except AssertionError:
    print("hi")
    raise Exception("eddie")
finally:
    print("bye")

"""
['total', 'num', 'items', 'reason', 'R1', 'R11', 'R2', 'date', 'out_reason', 'out_date', 'department']
"""