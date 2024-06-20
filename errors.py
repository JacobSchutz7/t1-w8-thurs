# Standard exception
## Index error: raised when a sequence subscript, like a list, is out of range. 
mylist = [1,2,3]
print(mylist[3])
## KeyError: raised when a dictionary key is not found.
my_dict = {
	'name': 'Rachel'
}
print(my_dict['age'])
## ValueError: raised when a function receives of the correct type but inapropriate value 
int("abc")
## TypeError: raised when an operation of function is applied to an object of inappropriate type. 
len(123)

# Attribute errors: raised when an attribute reference or assignment fails. 
NoneType = None
NoneType.abc 

# ZeroDivisionError: raised when the second operand of a division (denominator) or modular operation is zero. 
10 / 0

# OS errors: raised for system-related errors.
## FileNotFoundError: raised when trying to open a file that does not exist. Commonly caused by typos. 
open('random_file.txt')

# User defined exceptions: users create by subclassing the built-in Exception class. 
class MyCustomError(Exception):
	pass

raise MyCustomError("Hey mate! There is an error.")