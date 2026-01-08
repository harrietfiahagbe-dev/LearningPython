#Day 2: 30 Days of python programming
#Exercise 1
first_name= "Yayra"
last_name = "Fiahagbe"
full_name = "Harriet Yayra Boven Fiahagbe"
country = "Ghana"
city = "Elmina"
age = 19
year = 2026
is_married = False
is_true = True
is_light_on = True
name,age,church,mother,father = "Efua", 24, "Methodist", "Esi", "Ekow"


#Exercise 2
print(type(10))
print(type({"Church":"Methodist",
           "Name": "Harriet",
           "Number": "0598275534",
           }))
print(type((1,"elorm", "senam")))
print(type({"set",1,2,3,3}))# the set is able to make the 3 just one, remember no duplication
print(type(["ama","kofi", "aba", "adwoa"]))

print(len(first_name))
print(len(last_name))
num_one = 5
num_two = 4
total = num_one+num_two
diff = num_two-num_one
product = num_two*num_one
division = num_one/num_two
remainder = num_two%num_one
exp = num_one**num_two
floor_division = num_one//num_two

print(f"sum: {total}")
print(f"difference: {diff}")
print(f"product: {product}")
print(f"division: {division}")
print(f"Modulus: {remainder}")
print(f"Exponential: {exp}")
print(f"Floor Division: {floor_division}")

raduis = 30
pie = 3.14159
area_of_circle= pie* (raduis**2)
print(area_of_circle)
circum_of_circle = 2 * pie * raduis
print(circum_of_circle)
new_raduis = int(input("What is the raduis of your circle? "))#remember you have to put the datatype at the front
new_area = pie * (new_raduis**2)
#print("Your new area is: ", new_area)
print(f"Your new area is {new_area}") #this is the f string format, remember
name = input("What is your name?")
last = input("What is your last name?")
coun = input("What is your country?")
age = int(input("What is your age?"))
