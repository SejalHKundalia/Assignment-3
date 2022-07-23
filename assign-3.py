#1.	Why are functions advantageous to have in your programs?

"""Using functions, you do not need to repeat your codes, instead the same code can be called again and again with a simple function call.
This reduces the need of same code repetitively.
"""
#2.	When does the code in a function run: when it's specified or when it's called?

"""The function is executed on function call"""

#3.	What statement creates a function?
    """
    def func_name():
        code..
        ……….
    """
#4.	What is the difference between a function and a function call?
"""Function contains a block of code that can be run/executed on function call"""
"""
    Example:
    def func1(): # function
        print("Hello")

func1() # function call
"""

#5.	How many global scopes are there in a Python program? How many local scopes?

"""
In the example below, the scope of variable a is in the main body and so it has a global scope
In the example below, the scope of the variable a inside the function have local scope"""


"""
a = 11 # here a is the global variable
def func1():

    a =12 # Here a is a local variable
    print(a) # prints the value of a inside the function
func1()
print(a)# outside the function body so prints the global variable 
"""

# Note : You can change the local variable to global by using keyword: global
"""
Example

a = 11
def func1():

    global a =12 # variable a is a global variable
    print(a)
func1()
print(a)

"""

#6.	What happens to variables in a local scope when the function call returns?
    """ The scope of the variable expires outside the function """

#7. What is the concept of a return value? Is it possible to have a return value in an expression?
    """ 
    Any function can return a particular value or expression using the return keyword.
    Example:
    
    def add(a,b):
        return a+b
    
    X = add(5,6) # here X will contain the value returned by the function 
    """

#8. If a function does not have a return statement, what is the return value of a call to that function?

    """None Type"""

#9. How do you make a function variable refer to the global variable?

    """Using a keyword: global"""
    """  ex: global X"""

#10. What is the data type of None?
     """NOne Type"""


#11. What does the sentence import areallyourpetsnamederic do?

    """This statement imports module : areallyourpetsnamederic
    This will allow you to use all the functions and libraries of the module"""

#12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
    """import spam
        spam.bacon()"""

#13. What can you do to save a programme from crashing if it encounters an error?
     """ Use exception handling"""

#14. What is the purpose of the try clause? What is the purpose of the except clause?
      """
         Try and Except are the keywords of exception handling.
         Try : Contains the logic for a risky code.
         Except: It handles an error/exception occurred during code execution
      """