from user import User
class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        print("\nHere are the privileges an administrator has:")
        for privilege in self.privileges:
            print(" -"+privilege.title())
class Admin(User):
    def __init__(self, first_name, last_name, age, degree):
        super().__init__(first_name, last_name, age, degree)
        self.privileges = Privileges()
