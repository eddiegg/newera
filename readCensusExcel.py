import openpyxl,pprint,logging
logging.basicConfig(level=logging.DEBUG,format=('%(message)s'))
wb = openpyxl.load_workbook('./test/censuspopdata.xlsx')
sheet = wb.active
countyData={}
for row in range(2,sheet.max_row):
    state = sheet['B'+str(row)].value
    county = sheet['C'+str(row)].value
    pop = sheet['D'+str(row)].value
    countyData.setdefault(state,{})
    countyData[state].setdefault(county,{"tracts":0,"pop":0})
    countyData[state][county]["tracts"] += 1
    countyData[state][county]["pop"] += int(pop)
logging.debug(pprint.pformat(countyData))
with open('./census2010.py','w') as resultFile:
    resultFile.write('Data = ' + pprint.pformat(countyData))
