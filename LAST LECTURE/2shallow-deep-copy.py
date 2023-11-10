#Important Note:
#for 1d list deep and shallow both function in same way

import copy

#deep and shallow copy for 1d list
print('shallow copy for 1d list\n')
list = [1,2,3,4,5]
shalow_copied_list= copy.copy(list)
shalow_copied_list[1] = 23
shalow_copied_list[2] = 46
print('original  1D list :  ',list)
print('shallow copy 1D list :  ',shalow_copied_list)

print('shallow copy for 1d list\n')
list = [1,2,3,4,5]
copied_list= copy.deepcopy(list)
copied_list[1] = 23
copied_list[2] = 46
print('original list 1D list :  ',list)
print('copied_list 1D list :  ',copied_list)

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)
print()
old_list[1][1] = 'AA'
old_list.append([4, 4, 4])
print("Old list:", old_list)
print("New list:", new_list)
print(id(old_list))
print(id(new_list))

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'
old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)
print(id(old_list))
print(id(new_list))
