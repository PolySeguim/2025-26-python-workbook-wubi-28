# def is the keyword to define a function
# whatType is the name of the function
# userInput is the parameter of the function
def whatType(userInput):
    #print is a Python built-in function that prints to the console
    # type is a Python built-in function that finds the datatype
    # The program ignores all comments 
    # userInput is a variable that the user enters
    print(type(userInput))
  # The pound symbol is for one line comments
  # The program ignores all comments 
 
"""  
multiple line comments
 """
# Call the function with different user inputs
# If you don't call the function, nothing will run in the program

"""
Test SUITE
"""
""""""
whatType(3)
whatType(3.0)
whatType("3.0")
whatType(True)
whatType(Wubi)
whatType('w')

#Create a variable named message
message = """this is a 
multiline message
to my bestie."""
print(message)

#test inputs to print and see how they print
print(42000)
#every time you have a comma between values, it will understand as a different
#parameter input
print(42,"wubi", 3,"chem","computer")
print(42,000)
print(42.000)
