#! python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    # 行列互换的新列表
    ntable = list(map(list, zip(*table)))   \
    # 找到最长元素长度
    nline = []
    for line in ntable:
        nline.extend(line)
    sortedline = sorted(nline,key=len)
    maxLength = len(sortedline[-1])
    # 按照格式打印
    ll = len(ntable)
    ww = len(ntable[0])
    for i in range(ll):
        j = 0
        while j < (ww - 1):
            print(str(ntable[i][j]).rjust(maxLength), end='')
            j += 1
        print(str(ntable[i][-1]).rjust(maxLength))


printTable(tableData)
