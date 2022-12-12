#Chapter 5 - Exercise 2
#Store five programming words in a dictionary called glossary
glossary = {"variable": "a value that can change, depending on conditions or on information passed to the program.", 
"control statements": "statements that change the flow of execution of statements.",
"data structure": "a specialized format for organizing, processing, retrieving and storing data.",
"functions": "a “chunk” of code that you can use over and over again, rather than writing it out multiple times.",
"data": "information that has been translated into a form that is efficient for movement or processing."}
#Print each word and its meaning in a neatly formatted output:
for key, value in glossary.items():
    print(f"{key.title()}: \n\t{value}")
    print()