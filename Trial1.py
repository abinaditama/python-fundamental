# sum all items in list
def sum_item_list(list):
  x = 0
  for i in list:
    x += i
  return x
print(sum_item_list([1,2,3,4,5,6]))

# multiply all items in list
def mutiply_list (list):
  y = 1
  for i in list:
    y *= i
  return y
print(mutiply_list([1,3,5,6]))

# get largest number in list
def largest(list):
  list2 = sorted(list)
  largest = list2[-1]
  return largest
print(largest([1,3,6,7,8,9,-11,99]))

def smallest (list):
  listX = sorted(list)
  smallest = listX[0]
  return smallest
print(smallest([9,7,5,10,-11,-97,-3]))

def flatten (nums):
  listA = []
  for i in nums:
    for y in i:
      listA.append(y)
  return print(listA)

flatten([[2,4,3],[1,5,6], [9], [7,9,0]])



