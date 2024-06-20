# T1W8 Thursday

## 4 Pillars of OOP contd.

### __repr__ method
- Special method, like __init__, which is ised to define a string representation for an object. 
- Particularly used for debugging and development because it can give detailed info about an object. 

### Composition of OOP
- Design principle where a class is composed of one or more objects from other classes. 
- An alternative to inheritance. It is often times more flexible and modular. 
- Avoids inheritance's pitfall: changes in base class can unintentionally affect the derived class, which may break their functionality. 
- Composition does not directly affect the composed class, as the class inherits from component classes through well-defined interfaces. 

## Error Handling

### Taxonomy of Python Errors
- Silent logical errors: code that runs but are not working as intended. 
- Assertion Errors: raised when an assert statement fails. If condition is True, nothing happens. If false, assertion error is raised.
- Syntax Errors: raised when there is improper syntax in the code. In other words, the python interpreter can't understand your code and so raises an syntax error. 
- Exceptions: runtime errors

### Stack Trace Interpretation

### Try / Except / Finally
- Comprehensive way to handle exceptions
- Ensures code always runs, regardless wether an error occurs.
- 'try' block has code that may raise exception
- 'except' block has code that handles the exception
- 'finally' block has the code that should always be executed.