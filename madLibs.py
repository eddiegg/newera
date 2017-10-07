#! /usr/local/bin/python3
testFile = open('testFile')
content = testFile.read()
testFile.close()
contentList = content.split()
nounCount = contentList.count('NOUN')
noun = []
print(contentList)
print(contentList.index('ADJECTIVE'))
adj = input('Enter an adjective: ')
contentList[contentList.index('ADJECTIVE')] = adj
for i in range(nounCount):
    # noun.append(input('Enter a noun: '))
    contentList[contentList.index('NOUN')] = input('Enter a noun: ')
newContent = ' '.join(contentList)
testFile = open('testFile','w')
testFile.write(newContent)
testFile.close()
