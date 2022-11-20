def sandwich(*parts):
    print('Sandwich is consist of: ')
    for produkt in parts:
        print('- ' + produkt)

sandwich('onion')
sandwich('onion', 'cucumber', 'tomato', 'chiken')