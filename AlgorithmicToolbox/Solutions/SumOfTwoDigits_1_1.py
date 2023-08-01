def add_digits(num: list):
    """
    This function takes a list of integers as input and calculates the sum of the first two elements.

    Parameters:
        num (list): A list of integers. It is assumed to have at least two elements.

    Returns:
        None: The function doesn't return anything; it only prints the sum of the first two elements.

    Example:
        >>> numbers = [5, 7, 9, 2, 4]
        >>> add_digits(numbers)
        12
    """
    print(num[0] + num[1])

if __name__ == '__main__':
    # Read a line of space-separated numbers from the user input and convert them into a list of integers.
    numbers = list(map(int, input().split()))

    # Call the add_digits function to calculate and print the sum of the first two elements of the list.
    add_digits(numbers)

