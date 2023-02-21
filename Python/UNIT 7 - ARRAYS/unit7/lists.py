# Filename: lists.py

pets = ["Dog","Cat","Bird"]
print(pets)

# Using list indexes
print("Index 0",pets[0])
print("Index 1",pets[1])
print("Index 2",pets[2])
print("Index -1",pets[-1])
print("Index -2",pets[-2])
print("Index -3",pets[-3])
print("Pets length",len(pets))

# Mutating (changing) list
pets[2] = "Ferret"
print("Index 2 after mutate",pets[2])
repeated = pets * 3
print("Repeated",repeated)
print("Repeated length",len(repeated))

# Index Error - out of range
try:
    print("Index 5",pets[5])
except IndexError as message:
    print("Index 5:",message)

# List concatenation
fruits = ["Orange","Banana","Apple"]
meals = ["Ham","Burger"]
print("Fruits:",fruits)
print("Meals:",meals)
meals += fruits
print("Meals:",meals)
for food in meals:
    print("Food:",food)

# List Slicing
print("Meals:",meals)
print("Slice 2:4",meals[2:4])
print("Slice :2",meals[:2])
print("Slice -3:-2",meals[-3:-2])
print("Slice ::2",meals[::2])
print("Slice :len(meals):2",meals[:len(meals):2])
      
# Finding if item in list
if "Ham" in meals:
    print("Ham is in meals")
else:
    print("Ham is not in meals")

if "Peach" not in meals:
    print("Peach is not in meals")
else:
    print("Peach is in meals")

# List methods
meals.append("Potatoes")
print("Meals:",meals)
print("Index for Orange",meals.index("Orange"))
meals.insert(2,"Pear")
print("Meals:",meals)
meals.remove("Banana")
print("Meals:",meals)
meals.sort()
print("Meals:",meals)
meals.reverse()
print("Meals:",meals)
del meals[2]
print("Meals:",meals)

# Copying Lists
scores = [5,2,6,8,7,3]
print("Scores",scores)
print("Minimum",min(scores))
print("Maximum",max(scores))
topScores = scores
print("Top Scores:",topScores)
print("Scores    :",scores)
scores.remove(8)
print("Top Scores:",topScores)
print("Scores    :",scores)
scores = [5,2,6,8,7,3]
topScores = []
for aScore in scores:
    topScores.append(aScore)
print("Top Scores:",topScores)
print("Scores    :",scores)
scores.remove(8)
print("Top Scores:",topScores)
print("Scores    :",scores)
print("Index 5 item * index 2 item",topScores[5] * topScores[2])
totalScores = 0
for aScore in topScores:
    totalScores += aScore
print("Total Scores",totalScores)
print("Average",totalScores / len(topScores))

# Write to a file
listFile = open("scores.txt","w")

for aScore in topScores:
    listFile.write(str(aScore) + "\n")

listFile.close()
print("topScores saved to file scores.txt")

# Convert list to tuple
print(tuple(meals))


