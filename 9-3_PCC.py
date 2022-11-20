class User():
    def __init__(self, first_name, last_name, age, country):
        self.name = first_name
        self.surname = last_name
        self.age = age
        self.country = country
    def describe_user(self):
        print('User name: ' + self.name.title() + '.' +
              '\nUser surname: ' + self.surname.title() + '.' +
              '\nUser age: ' + self.age + '.' +
              '\nUser country: ' + self.country.title() + '.')
    def greet_user(self):
        print('Hello, ' + self.name.title() + "!")

kyrylo = User('kyrylo', 'lanovyi', '26', 'Ukraine')
suan = User('suan', 'hen hao', '25', 'China')
kyrylo.describe_user()
kyrylo.greet_user()

suan.describe_user()
suan.greet_user()