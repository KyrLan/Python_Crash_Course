def make_great(names, great_names):
    while names:
        great = str ('Great ' + names.pop(0))
        great_names.append(great)

f_names = ['Kurulo', 'Vlada', 'Sasha', 'Oleg']
new_f_names = []
make_great(f_names, new_f_names)
print(f_names)
print(new_f_names)