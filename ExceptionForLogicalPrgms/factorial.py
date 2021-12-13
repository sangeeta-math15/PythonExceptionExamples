def recur_factorial(n):
    """
    :param n:
    :return:
    """
    if n == 1:
       return n
    else:
       return n*recur_factorial(n-1)

try:
        # take input from the user
        num = int(input("Enter a number: "))
        # check is the number is negative
        if num < 0:
            raise ValueError("That is not a positive number!")
        elif num == 0:
            raise ValueError("The factorial of 0 is 1")
except ValueError as ve:
    print(ve)

else:
       print("The factorial of ",num,"is",recur_factorial(num))

