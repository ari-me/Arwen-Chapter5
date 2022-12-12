#Chapter 5 - Exercise 4
#Write 3 major rivers as the keys and its countries as the value in a dictionary
river = {"yangtze": "china", "ganges": "india", "congo": "africa"}
for key, value in river.items(): #Looping through the dictionary
    print(f"The {key.title()} River runs through {value.title()}.")
print("\nThe rivers in the list are:")
for key in river.keys(): #Looping through the rivers
    print(f"\t {key.title()} River")
print("\nThe countries in the list are:")
for value in river.values(): #Looping through the countries
    print(f"\t {value.title()}")