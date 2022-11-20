filename = "learning_python .txt"

print ('\nThe firs variant:')
with open (filename) as file:
    f_var = file.read()
    print (f_var)

print('\nThe second variant:')
with open (filename) as s_file:
    for s_line in s_file:
        print (s_line.rstrip())

print('\nThe third variant:')
with open(filename) as t_file:
    lines = t_file.readlines()
for line in lines:
    print (line.rstrip())