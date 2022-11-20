class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    def describe_restaurant(self):
        print('Restaurant' + "'" 's name is ' + self.name.title() + '!')
        print('The cuisine type is ' + self.type.title() + '.')
    def open_restaurant(self):
        print('Restaurant ' + self.name.title() + ' is open.')


restaurant = Restaurant('Quine', 'Asian food')
print('Restaurant with name ' + restaurant.name.title() + ' has an '
      + restaurant.type.title() + ' cuisine.')
restaurant.describe_restaurant()
restaurant.open_restaurant()