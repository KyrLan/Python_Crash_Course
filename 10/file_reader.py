text_path = 'pi_digits.txt'
with open(text_path) as file_object:
    content = file_object.readlines()
    print(content)

pi_string = ''
for line in content:
    pi_string += line.strip()
print (pi_string)