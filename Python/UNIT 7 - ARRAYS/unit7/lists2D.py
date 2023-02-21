# Filename: list2D.py

people = []
people.append(["Goofy",10])
person = ["Mickey",12]
people.append(person)
print(people)
print(people[0])
print(people[1][0])

for aPerson in people:
    for detail in aPerson:
        print("Detail",detail)
        
