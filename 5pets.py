#Chapter 5 - Exercise 5
#Make several dictionaries with each representing a different pet
pet1 = {"animal type": "dog", "pet name": "Chewy", "owner": "Kate"}
pet2 = {"animal type": "snake", "pet name": "Anne", "owner": "Ray"}
pet3 = {"animal type": "owl", "pet name": "Norman", "owner": "Emma"}
#Store the dictionaries in a list
pets = [pet1, pet2, pet3] 
for p in pets: #loop through the list and print everything
    print("This is the information on", p["pet name"])
    print(f"{p}\n")