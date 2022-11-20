class User():
    def __init__(self, first_name, last_name, age, country):
        self.name = first_name
        self.surname = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0
    def describe_user(self):
        print('User name: ' + self.name.title() + '.' +
              '\nUser surname: ' + self.surname.title() + '.' +
              '\nUser age: ' + self.age + '.' +
              '\nUser country: ' + self.country.title() + '.')
    def greet_user(self):
        print('Hello, ' + self.name.title() + "!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0