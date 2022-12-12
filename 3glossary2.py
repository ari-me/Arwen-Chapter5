#Chapter 5 - Exercise 3
#Using the same code from chapter 2, add 5 more terms to your glossary
glossary = {"data": "information that has been translated into a form that is efficient for movement or processing.", 
"string": "a series of characters.",
"variable": "a value that can change, depending on conditions or on information passed to the program.", 
"boolean expression": "an expression that evaluates True or False.",
"operator": "a character that represents a specific mathematical or logical action or process.",
"nested": "code that performs a particular function and that is contained within code that performs a broader function.",
"control_statements": "statements that change the flow of execution of statements.",
"loop": "a sequence of instruction s that is continually repeated until a certain condition is reached.",
"data structure": "a specialized format for organizing, processing, retrieving and storing data.",
"functions": "a “chunk” of code that you can use over and over again, rather than writing it out multiple times.",
}
#Using a loop, run through your dictionary
for key, value in glossary.items():
    print(f"{key.title()}: \n\t{value}")
    print()