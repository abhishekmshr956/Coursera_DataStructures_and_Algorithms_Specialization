import sys

def MaxPairwiseProductNaive(a: list) -> int:
    """ Calculate the maximum product of two numbers at distinct positions from a list of integers.
    
    Parameters:
    a (list): A list of integers
    
    Returns:
    product (int): The maximum product of two numbers at distinct postions
    
    Example:
        >>> a = [7, 4, 8, 5]
        >>> product = Naive_max(n, a)
        >>> print(product)
        56
    """
    n = len(a)
    product = 0 # stores the max product
    
    for i in range(n):
        for j in range(i+1, n):
            product = max(product, a[i]*a[j])
    return product

def MaxPairwiseProductFast(a: list) -> int:
    n = len(a)
    ix_1 =0 
    for i in range(1, n):
        if a[i] > a[ix_1]:
            ix_1 = i
    temp = a[-1]
    a[-1] = a[ix_1]
    a[ix_1] = temp
    if ix_1 == 0:
        ix_2 = 1
    else:
        ix_2 = 0
    for i in range(1, n):
        if i != ix_1 and a[i] > a[ix_2]:
            ix_2 = i
    product = a[ix_1] * a[ix_2]
    return product

def read_dataset(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            integer_list = list(map(int, content.split()))
            return integer_list
        
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path: {file_path}")

    except Exception as e:
        print(f"Error occurred while reading the file: {str(e)}")
        return None
    
if __name__== '__main__':
    #n = int(input()) # read the number of elements in the array
    # a = list(map(int, input().split())) # read a line of space separated numbers and convert them to list of integers

    # check if the filename is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python MaxPairwiseProduct_1_2.py dataset.txt")
    else:
        file_path = sys.argv[1]
        a = read_dataset(file_path)
        if a is not None:
            product = MaxPairwiseProductFast(a)
            print(product)