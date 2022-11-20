class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print('Restaurant' + "'" 's name is ' + self.name.title() + '!')
        print('The cuisine type is ' + self.type.title() + '.')
    def open_restaurant(self):
        print('Restaurant ' + self.name.title() + ' is open.')
    def set_number_served(self, served):
        self.number_served = served
    def increment_number_served(self, increase):
        self.number_served += increase

restaurant = Restaurant('Quine', 'Asian food')
restaurant.set_number_served(24)
restaurant.increment_number_served(10)
print('Restaurant with name ' + restaurant.name.title() + ' has an '
      + restaurant.type.title() + ' cuisine.' +
      '\nToday the restaurant has ' + str(restaurant.number_served) + ' visitors')

