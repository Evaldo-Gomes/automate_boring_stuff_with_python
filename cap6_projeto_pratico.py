tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


a = [0]*len(tableData)
b = [1]*len(tableData)
c = [2]*len(tableData)

print(a)
print(b)
print(c)

x = (str(tableData[0])).split()
y = (str(tableData[1])).split()
z = (str(tableData[2])).split()

def printTable():
    colWidth = [0] * len(tableData)


    
    
