# sum all list item
list1 = [-4,-3,1,5,7,9,-4]
x = 0
print(f'List will be added = {list1}')
for i in list1:
    x += i
print(f'addition result is {x}')
print('\n')

# multiply all the items in a list
print(f'list to be multiplied {list1}')
y = 1
for i in list1:
    y = y*i
print(f'multiplication result is {y}')
print('\n')

# largest number in list
print('largest number in list1')
z = list1[0]
for i in range(len(list1)):
    if list1[i] > z:
        z = list1[i]
print(f'largest number is {z}')
print('\n')

# largest number in list
print('smallest number in list1')
z = list1[0]
for i in range(len(list1)):
    if list1[i] < z:
        z = list1[i]
print(f'smallest number is {z}')
print('\n')

'''count the number of strings where the string 
length is 2 or more and the first 
and last character are same from a given list of strings'''

list2 = ['abc', 'xyz', 'aba', '1221']
print(list2)
counter = 0
for i in list2:
    if len(i)>2:
        if i[0] == i[-1]:
            counter +=1
print(f'string length more than 2 character, first and last char are same {counter}')
print('\n')

list3 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(len(list3)-1):
    for j in range(i, len(list3)):
        if list3[i][1] > list3[j][1]:
            abc = list3[i]
            list3[i] = list3[j]
            list3[j] = abc
print(list3)
