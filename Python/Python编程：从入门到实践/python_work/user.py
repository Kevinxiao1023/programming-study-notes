class User():
    def __init__(self, first_name, last_name, age, degree):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.degree = degree
        self.login_attempts = 0
    def describe_user(self):
        print("\nYour name is "+self.first_name.title()+" "+self.last_name.title()+", you are "+str(self.age)
              +" years old. You have got a "+self.degree.title()+" degree.")
    def greet_user(self):
        print("Hello, "+self.first_name.title()+" "+self.last_name.title()+", good day!")
    def read_login_attempts(self):
        print("The number of login attempts is "+str(self.login_attempts)+".")
    def increment_login_attempts(self):
        self.login_attempts+= 1
    def reset_login_attempts(self):
        print("\nResetting the login attempts....")
        self.login_attempts = 0
