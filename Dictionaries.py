my_dict = {}
my_dict['Jan'] = 31
my_dict['Feb'] = 28
my_dict['Mar'] = 31
print(my_dict)

my_dict2 = {'Apr': 31, 'May': 30, 'Jun': 31}
print(my_dict2)

#1st way of printing items inside dict(list with tuples inside includes key and value)
items_view = my_dict2.items()
print(items_view)

#2nd way - key value
for key, value in my_dict.items():
    print(key, value)

#3rd way - key=value
for key, value in my_dict2.items():
    print(f'{key}={value}')

#printing only keys
for key in my_dict2.keys():
    print(key)

#printing only values
for value in my_dict2.values():
    print(value)

#getting sum of values
print(sum(my_dict2.values()))

#OR
sum = 0
for value in my_dict.values():
    sum += value

print(sum)

print('------------------------------------------------------------')
# Excerise
my_text = 'In a competitive research environment, publishing is not enough anymore. You have to make your research accessible, findable and visible. Your online identity is the central key for your career and your recognition, particularly for young researchers. This session will help you to build your online research profile by applying best practices. You will learn how to evaluate your online identity and promote your work by using the tools best suited to your needs. A special focus on ORCID will be presented.'

#TODO
# 1. Delete special symbols (.,",')
# 2. Create a dictionary containing each word and the number of occurences (count)

#1.
replace_pairs = {"'":'', ',':'', '.':''}
for old_value, new_value in replace_pairs.items():
    my_text = my_text.replace(old_value, new_value)
print(my_text)

#2.
from collections import Counter
words_split_counter = Counter(my_text.split())
words_dict = dict(words_split_counter)
print(words_dict)






