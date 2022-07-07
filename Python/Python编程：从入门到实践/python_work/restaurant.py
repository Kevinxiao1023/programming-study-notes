class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("Our restaurant is called "+self.restaurant_name.title()+", and it provides "+
              self.cuisine_type.title()+" cuisine!")
    def open_restaurant(self):
        print("Come on in, we are open!")
    def read_number(self):
        print("There are "+str(self.number_served)+" people enjoy their food here!")
    def set_number_served(self, number):
        self.number_served = number
    def increment_number_served(self, add_number):
        print("\nThe actual number of the people served everyday is about to change...")
        self.number_served+= add_number
