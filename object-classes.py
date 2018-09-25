#objects and classes
class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.no_of_greeting = 0
#---------__repr__---------------------------------
    def __repr__(self):
        return "Hello, I am {0}. I would like to contact you via my email address which is {1}. In case you are unable to reach out to me via email, here is my phone number {2}".format(self.name,self.email,self.phone)


#add a friend method-------------------------------
    def add_friend(self,friend):
        return self.friends.append(friend)

#add a number of friends method

    def num_friend(self):
        print(len(self.friends))
#count number of greetings-------------------------

    def print_contact_info(self):
        print("Sonny's email: %s, Sonny's phone number: %s" % (self.email, self.phone))


#
    def greet(self, other_person):
        print('Hello %s, I am %s!' % (other_person.name, self.name))
        self.no_of_greeting += 1

    def greeting_count(self):
        print("Greeted %s times" % (self.no_of_greeting))

#
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
print(sonny.print_contact_info())

jordan.add_friend("sonny")
print(jordan.friends)
sonny.add_friend("jordan")
print(sonny.friends)
#print(len(jordan.friends))
print(sonny.num_friend)
jordan.greet(sonny)
jordan.greet(sonny)
jordan.greet(sonny)
jordan.greet(sonny)
jordan.greeting_count()

print(jordan)
# jordan.friends.append("emre")
# sonny.friends.append("beyza")
# print(jordan.friends)
# print(sonny.friends)
# len(jordan.friends)
# print(len(jordan.friends))
# sonny.greet(jordan)
# jordan.greet(sonny)

# print(sonny.email)
# print(sonny.phone)
# print(jordan.email)
# print(jordan.phone)

#----------------------Make your own class------------------

# class Vehicle():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#
# #print(car.make,car.model,car.year)
#
#     def print_info(self):
#         print("%s, %s, %s" %(self.year, self.make, self.year))
# car = Vehicle("Nissan", "Leaf", "2015")
# car.print_info()
