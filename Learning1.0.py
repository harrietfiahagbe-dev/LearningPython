#INTRODUCTION
'''
print("Hello, Welcome to Learning Python!")
print(3+5) #ADDITION
print(8+10) #SUBTRACTION
print(10-7) #SUBTRACTION
print(9*8) #MULTIPLICATION
print(3/2)
print(3**2) #Exponential value
print(10%3)#Modulus (Gives the remainder when smth is dividing smth)
print(12//5) #Floor division sign, removes the decimal attached to it


#CHECKING DATA TYPES
print(type(10)) #int
print(type(3.4)) #float
print(type(3 +4j)) #complex number
print(type("Yayra")) #string
print(type([1,2,2])) # list: they are ordered, because of the index and they are mutable can be changed easily, can have other datat types, including lists,int etc. use sqaure braket for list
print(type({"Name" : "Yayra"})) #dictionary, they are unordered pairs, can be selected only from keys and values, no index, the keys have to be unique, we have to use curly bracket for dictionaries, they are mutable as well
print(type({3,7,8.9})) #set, they are unique and mutable, no duplicates in the values, and they are unordered (index? : yes no index that is why they are unordered), also uses curly brackets, can contain all data types excepts from dictionaries and lists
print(type((1,2,2)))#ordered, and they are immutable, cannot change when it has been placed in the brackets, can hold different dtat type


#VARIABLES AND BUILT IN FUNCTIONS
#Make use of built in functions without importing or configuring
first_name = "Yayra"
country = "Ghana"
skills = ["java", "python", "geogebra", "vsco"]
my_info = {"Name" : "Yayra",
           "Age" : 19,
           "City" : "Elmina",
           "Sisters" : "Elorm,Senam"
           }
print(len(first_name))
print("Name:",first_name)
print("Country:" ,country)
print("My Info: ", my_info)

#Declaring muitple variables in one line
name, age, school, grade = "Boven", 19, "Ashesi", "A+"
print("New Name:" , name )
print("New Age:" , age)
print("Uni:" ,school)
print("Grade" , grade)

name_info = input("What is your name?")
age_info = input("What is your age?")
print(name_info)
print(age_info)
'''

#Casting
#int to float
num_int = 10
print("Int Num:", num_int)
num_float = float(num_int)
print("Float Num:",num_float )

#float to integer
new_num = 5.67
int_num = int(new_num)
print("Conversion:", int_num)

#int to str
#using num_int
num_str = str(num_int)
print("String Number: ", num_str)

#Str to int or float
num_str = "10.6"
float_num = float(num_str)
print("Float Number", float_num)
new_intone = int(float_num)
print("Integer", new_intone)# so we can change from string to float, then from float to string, we cant directly change from string to int

#str to list
name_str = "Yayra"
list_name = list(name_str)
print("List in Names", list_name)