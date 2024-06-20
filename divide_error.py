def divide_numbers():
    try:
        # Get input from the user
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))

        # Perform the division
        result = dividend / divisor
        print(f"Result of division: {result}")

    except Exception as e:
        print(f"An unexpected error occured: {e}")
    finally:
        print("Division operation closed.")

# Perform the division
divide_numbers()