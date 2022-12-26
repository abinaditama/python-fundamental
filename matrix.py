row = int(input('jumlah baris : '))
column1 = int(input('jumlah kolom1 : '))
column2 = int(input('jumlah kolom2 : '))

matrix = []
listA = []
listB = []

for i in range(row):
    list1 = []
    for j in range(column1):
        list1.append(input('masukkan angka : '))
    listA.append(list1)
matrix.append(listA)

for i in range(row):
    list2 = []
    for x in range(column2):
        list2.append(input('masukkan angka : '))
    listB.append(list2)
matrix.append(listB)

print(matrix)

''' for i in range(row):
    for j in range(column1):
        print(matrix[i][j], end=' ')
    print('') '''


