my_dict = {'name': 'Jack', 'age': 26, 'age': 45, 'wage': 57000}
my_dict['cell'] = '03003003003'
my_dict['pm'] = 'imran khan'
'''for i in my_dict.keys():
    print(i)'''
print(my_dict['name'])
print(my_dict.get('name'))
'''
                  DICITIONARY KEYS AND VALUES
    *VALUES
        (i) any type,can be duplicte
        (ii) can be list or even another dictuonary
    *KEYS
        (i)must unique
        (ii)immutabletype(int,float,string,tuple,bool)
        note:
        be careful while using float as key
    * no order in dictionary
    
'''
#print(my_dict[1])
print(my_dict.keys())
print(my_dict.values())

for i in my_dict:
    print(my_dict[i])
print("<-------------------------------->")
my_iter = iter(my_dict)
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
list = [8] * 3
sum =0
"""
            LIST                    DICTIONARY
    ORDERED                         NO ORDER
"""

#function to finds frequency of words
def str2dictionary(string):
    my_dict = {}
    for word in string:
        if word in my_dict:
            my_dict[word]+=1

        else:
            my_dict[word] = 1
    return my_dict


print(str2dictionary("sssshhhhjdfs"))

#find common words
