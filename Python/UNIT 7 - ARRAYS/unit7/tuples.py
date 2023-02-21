# Filename: tuples.py

pets = ("Dog","Cat","Bird")
print("Pets",pets)
print("Pet 0",pets[0])
print("Pet 1",pets[1])
print("Pet 2",pets[2])
print("Pet -1",pets[-1])
print("Pet -2",pets[-2])
print("Pets length",len(pets))

try:
    pets[2] = "Ferret"
except TypeError as message:
    print(message)
print("Pets",pets)

repeated = pets * 3
print("Repeated",repeated)

fruits = ("Orange","Banana","Apple")
meals = ("Ham","Burger")
print("Fruits",fruits)
print("Meals",meals)
meals += fruits
print("Meals",meals)

for food in meals:
    print("Food",food)

print("Slice 2:4",meals[2:4])
print("Slice :2",meals[:2])
print("Slice -3:-2",meals[-3:-2])
print("Slice ::2",meals[::2])

# Finding if item in list
if "Ham" in meals:
    print("Ham is in meals")
else:
    print("Ham is not in meals")

if "Peach" not in meals:
    print("Peach is not in meals")
else:
    print("Peach is in meals")

#meals.append("Potatoes")
print("Index for Orange",meals.index("Orange"))

# Convert a tuple to list
print(list(meals))
