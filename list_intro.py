names = ["Zariah", "yakubu", "Tinubu", "Mohammad", "Balewa", "Dorcas"]
names.sort()
print(names)
#Checking the length 

# print(f"We now have {length_of_names} names in the list.")
#Adding new names to the list
names.append("favour")
names.append("Ade")
length_of_names = len(names)
print(f"We now have [{length_of_names}] names in the list.")
print(names)
# Removing names from the list 
names.remove("Balewa")
print(names)
cars = ["Toyota", "Honda", "Lexus", "Mercedes", "BMW"]
cars.insert(1, "Tesla")
print(cars)
cars.pop(2)
print(cars)