# math but bad. dont use

# no integers, comparative operators, while, for, boolean operators (besides not), math operators, data structures (besides tuples from definitions)

# non expandable circuits
def adder(a : int, b : int, c : int):
    """single bit adder circuit

    Args:
        a (int): addend 1
        b (int): addend 2
        c (int): carry in

    Returns:
        _type_: sum, carry out
    """
    
    return (a ^ b) ^ c, ((a ^ b) & c) | (a & b) # returns s, c

def xor(a : int, b : int) -> int:
    """outputs xor of bit a and bit b

    Args:
        a (int): bit 1
        b (int): bit 2

    Returns:
        int: xor of a and bit
    """
    
    return (a & (not b)) | ((not a) & b)

# odd circuits
def get_bit(a : int, place : int) -> int:
    """gets the bit at the desired place of bits a

    Args:
        a (int): any number of bits
        place (int): the desired bit, if over, will return zero

    Returns:
        int: the bit of a at index place, zero indexed
    """
    
    if place: return get_bit(a >> True, subtract(place, True))
    return a & True
    
def count_bits(a : int) -> int:
    """counts the bits of the given argument

    Args:
        a (int): any number of bits

    Returns:
        int: number of bits used to store variable a
    """
    
    if not a >> True: return True
    return add(count_bits(a >> True), True)
    
def ander(a : int, bit : int) -> int:
    """returns the value of each digit of a when applied to the AND operator with the given bit.

    Args:
        a (int): multibit 
        bit (int): single bit

    Returns:
        int: 0 if the bit is off, a if the bit is on
    """
    
    if bit: return a
    return False

def ones_compliment(a : int) -> int:
    """gets the ones compliment of a number without python interpreting it as a negative value.

    Args:
        a (int): positive constant

    Returns:
        int: ones compliment of given number using the number of bits of the number.
    """
    
    if not a >> True: return not a
    return ones_compliment(a >> True) << True | (not a & True)

def reverse_bits(a : int, bit : int) -> int:
    """reverses the bits of the variable a

    Args:
        a (int): any number of bits
        bit (int): the length of the bits (zero indexed)

    Returns:
        int: the reversed order of bits a
    """
    
    if not bit: return a & True
    return reverse_bits(a, subtract(bit, True)) << True | get_bit(a, bit)

def carry_subtractor(a : int, b : int, c : int = True) -> tuple[int]:
    """performs subtrcaction and returns the carry out. breaks for negative values

    Args:
        a (int): minuend
        b (int): subtrahend
        c (int, optional): carry in, used for recursion. Defaults to True.

    Returns:
        tuple[int]: difference, carry out
    """
    
    # gets first bit
    a0, b0 = a & True, not b & True
    
    # computes sum for the bit
    d, c = adder(a0, b0, c)
    
    # adjusts parts
    a, b = a >> True, b >> True
    
    # return diff
    if not a | b: return d, c
    d_next, c = carry_subtractor(a, b, c)
    return d_next << True | d, c

def restore_subtractor(a : int, b : int, c : int = True) -> tuple[int]:
    """performs subtraction and restores the original value if the difference is negative

    Args:
        a (int): minuend
        b (int): subtrahend
        c (int, optional): carry in, used in recursion. Defaults to True.

    Returns:
        tuple[int]: difference, carry out
    """
    
    d, c = carry_subtractor(a, b, c)
    if c: return d, c
    return a, c

def remove_first_bit(a : int) -> int:
    """removes the first bit of a

    Args:
        a (int): a positive constant

    Returns:
        int: the value of a without its first binary digit
    """
    
    if not a >> True: return False
    return remove_first_bit(a >> True) << True | (a & True)

# other math circuits
def pow(a : int, exp : int) -> int:
    """returns the result of a constant to the power of another constant

    Args:
        a (int): constant
        exp (int): exponent

    Returns:
        int: a to the power of exp
    """
    
    # if b is 0
    if not exp: return True
    return multiply(a, pow(a, subtract(exp, 1)))

def factorial(a : int) -> int:
    """factorial of constant a

    Args:
        a (int): starting factorial constant

    Returns:
        int: the value of the constant a
    """
    
    if not a: return True
    return multiply(a, factorial(subtract(a, 1)))

# multibit arithmetic circuits
def add(a : int, b : int, c : int = False) -> int:
    """adds addend a and addend b. not restricted to a set number of bits. 

    Args:
        a (int): addend 1 
        b (int): addend 2
        c (int, optional): carry in, used for recursion. Defaults to False.

    Returns:
        int: sum of values a and b.
    """
    
    # selects first bit
    a0, b0 = a & True, b & True
    
    # computes sum for the bit
    s, c = adder(a0, b0, c)
    
    # adjusts parts
    a, b = a >> True, b >> True
    
    # return sum
    if not a | b: return c << True | s
    return add(a, b, c) << True | s

def subtract(a : int, b : int, c : int = True) -> int:
    """the difference between minuend a and subtrahend b. not restricted to a set number of bits. breaks of diffenece is negative.

    Args:
        a (int): minuend
        b (int): subtrahend
        c (int, optional): carry in, used for recirsion. Defaults to True.

    Returns:
        int: difference between a and b.
    """
    
    # gets first bit
    a0, b0 = a & True, not (b & True)
    
    # computes sum for the bit
    d, c = adder(a0, b0, c)
    
    # adjusts parts
    a, b = a >> True, b >> True
    
    # return diff
    if not a | b: return d
    return subtract(a, b, c) << True | d
    
def multiply(a : int, b : int) -> int:
    """product of multiplicand a and multiplier b

    Args:
        a (int): multiplicand
        b (int): multiplier

    Returns:
        int: product of a and b
    """
    
    # first multiplication
    b0 = b & True
    a_and = ander(a, b0)
    c0 = a_and & True
    
    # if multiplying by one digit
    if not b >> True: return a_and
    
    # start multiply loop
    return multiply_loop(a, b >> True, a_and) << True | c0

def multiply_loop(a : int, b : int, a_prev : int) -> int:
    """used for the recursive loop when multiplying. 

    Args:
        a (int): multiplicand
        b (int): multiplier
        a_prev (int): previous multiplicand from past iteration

    Returns:
        int: product of a and b
    """
    
    # ander
    b0 = b & True
    a_and = ander(a, b0)
    tot = add(a_prev >> True, a_and, False)
    c0 = tot & True
    
    # if multiple was last bit
    if not b >> True: return tot
    
    return multiply_loop(a, b >> True, tot) << True | c0

def remainder_divide(D : int, d : int) -> tuple[int]:
    """returns the remainder and quotient of a divison operation

    Args:
        D (int): dividend
        d (int): divisor

    Returns:
        tuple[int]: quotient, remainder
    """
    
    # retrieves bits from division in a reversed state without correct shifting
    q, r = divide_loop(D, d, False, subtract(count_bits(D), True))
    
    # corrects quotient
    quo = reverse_bits(q, subtract(count_bits(q), True))
    diff_bits = subtract(count_bits(D), count_bits(q))
    quo = multiply(quo, pow(2, diff_bits))
    
    return quo, r

def modulus(D : int, d : int) -> int:
    """takes the modulus of the given division

    Args:
        D (int): dividend
        d (int): divisor

    Returns:
        int: remainder
    """
    
    return remainder_divide(D, d)[1]

def int_divide(D : int, d : int) -> int:
    """returns the quotient of the given division without any decimal places

    Args:
        D (int): dividend
        d (int): divisor
        
    Returns:
        int: quotient as integer
    """
    
    return remainder_divide(D, d)[0]

def divide_loop(D : int, d : int, diff : int = False, bit : int = False) -> tuple[int]:
    """main recursion loop for the division operation

    Args:
        D (int): dividend
        d (int): divisor
        diff (int, optional): previous difference from restore subtraction, used for recursion. Defaults to False.
        bit (int, optional): current bit of the dividend that is being used for division, used for recursion. Defaults to False.

    Returns:
        tuple[int]: carry out, difference or restoration
    """
    
    D0 = get_bit(D, bit)
    
    # completes division by using subtraction, shifting, and restoration
    d0, c0 = restore_subtractor((diff << True) | D0, d)
    
    if not bit: return c0, d0
    c1, d1 = divide_loop(D, d, d0, subtract(bit, True))
    return c1 << True | c0, d1
    
# working math operators
print('divide', int_divide(5256, 956))
print('mod', modulus(5256, 956))
print('add', add(5, 3))
print('subtract', subtract(23, 17))
print('multiply', multiply(14, 10))
print('pow', pow(3, 4))
print('factorial', factorial(5))
