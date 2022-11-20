from collections import OrderedDict
dictionary = {}
dictionary['tuple'] = 'кортеж'
dictionary['dictionary'] = 'словник'
dictionary['list'] = 'список'
dictionary['functions'] = 'функції'
print (type(dictionary))

for key, value in dictionary.items():
    print(key.title() + ' - ' + value.title())
print (dictionary is dict)
