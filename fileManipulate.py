import os,shelve
myFiles = ['testReport.xlsx','summary.docx','notes.txt']
for filename in myFiles:
    print(os.path.join('D:\\',filename))

# shelfFile = shelve.open('mydata')
# shelfFile['myFiles'] = myFiles
# shelfFile.close

with shelve.open('mydata') as shelfFile:
    print(type(shelfFile))
    print(shelfFile['myFiles'])
