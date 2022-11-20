from collections import OrderedDict
dictionary = OrderedDict()
dictionary['tuple'] = 'кортеж'
dictionary['dictionary'] = 'словник'
dictionary['list'] = 'список'
dictionary['functions'] = 'функції'

for key, value in dictionary.items():
    print(key.title() + ' - ' + value.title())
