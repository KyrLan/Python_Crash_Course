from user import User
class Privilege():
    def __int__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print('Admin has privileges such as:')
        privileges = ['permission to delete users', 'permission to add messages', 'permission to ban users']
        for i in privileges:
            print(i)

class Admin (User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.pr = Privilege()