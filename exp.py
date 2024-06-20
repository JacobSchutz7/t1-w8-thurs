# define a function to convert input to an integer
def convert_to_integer(value):
	try:

		result = int(value)
		print(f'Conversion Successful Result: {result}')
	except ValueError:
		print("That's not a number!")

# get user input
user_input = input("Enter a number to convert to integer: ")

# call function to convert to integer
convert_to_integer(user_input)

