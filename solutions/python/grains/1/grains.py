def square(number: int) -> int:
    
    """Return the number of grains on the given square of a chessboard."""
    
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)
    


def total():

    """Return the total number of grains on all 64 squares of a chessboard."""
    
    return 2 ** 64 - 1
