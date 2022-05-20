
'''Assignment 1
This assignment covers your basic profiency with
    Python. It engages your ability to transform
    data without affecting anything outside the program.
This assignment places heavy emphasis on basic Python constructs.
'''

def factorial(x):
    '''Item 1.
    Factorial. 1 point.

    Returns the factorial of an integer.
    An integer's factorial is the product of the integer and all
        integers below it.
    Parameters
    ----------
    x: int
        the integer whose factorial to return
    Returns
    -------
    integer
        the factorial of the argument
    '''
    # Write your code below this line

def factorial(x):

x = int(input('Enter Your Number Here:'))
factorial=1

if x>0:
    for n in range (1, x + 1):
        factorial = factorial*n

    print ("Factorial of", x , "is", factorial)

elif x==0:

    print ("Factorial of 0 is 1")

else:
    print("There are no factorials for a negative number")



def classify_grade(number_grade):


    '''Item 2.
    Classify Grade. 2 points.

    Returns the letter grade equivalent of a number grade.
    For this item, use these letter grade buckets:
        A: 92-100
        B+: 86-91.9
        B: 80-85.9
        C+: 74-79.9
        C: 67-73.9
        D: 60-66.9
        F: 0-59.9
    Parameters
    ----------
    number_grade: float
        the number grade to convert into a letter grade.
    Returns
    -------
    str
        the letter grade equivalent of the number grade.
    '''
    # Write your code below this line

def classify_grade(number_grade):

grade = float(input("Enter Score Grade Here:"))


if grade >=92 and grade <=100:
    print ("A")

elif grade >= 86 and grade<= 91.9:
    print ("B+")

elif grade >= 80 and grade <= 85.9:
    print ("B")

elif grade >= 74 and grade <= 79.9:
    print ("C+")

elif grade >= 67 and grade <= 73.9:
    print ("C")

elif grade >= 60 and grade <= 66.9:
    print ("D")

elif grade >= 0 and grade <= 59.9:
    print ("F")



def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):
    '''Item 3.
    Average Weight. 3 points.

    You have purchased two bags of items.
    The first bag contains one type of item, and the second bag contains another type.
    Return the weighted average weight of the items.

    Parameters
    ----------
    item_quantity_1: int
        the quantity of items in the first bag.
    item_weight_1: float
        the weight of each individual item in the first bag.
    item_quantity_2: int
        the quantity of items in the second bag.
    item_weight_2: float
        the weight of each individual item in the second bag.
    Returns
    -------
    float
        the weighted average weight of one item.
    '''
    # Write your code below this line

def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):

item_quantity_1 = int(input("enter item 1 quantity here:"))

item_weight_1 = float(input("enter item 1 weight here:"))

item_quantity_2 = int(input("enter item 2 quantity here:"))

item_weight_2 = float(input("enter item 2 weight here: "))

avg = ((item_quantity_1 * item_weight_1) + (item_quantity_2 * item_weight_2))/ (item_quantity_1 + item_quantity_2)

print(avg)


def string_sum(string):
    '''Item 4.
    String Sum. 3 points.

    Returns the sum of the digits provided in a string.
    For this item:
        1. Sum the digits contained in the string.
        2. Ignore any non-digit characters contained in the string.
    Parameters
    ----------
    string: str
        a string that can contain any character.
    Returns
    -------
    int
        the sum of the digits contained in the string.
    '''
    # Write your code below this line

    def string_sum(string):

        sum_digit = 0

    for x in string:

        if x.isdigit() == True:

            z = int(x)

            sum_digit = sum_digit + z

    return sum_digit

    print(string_sum("143Sushi"))



def distance(x_1, y_1, x_2, y_2):
    '''Item 5.
    Distance. 3 points.
    Returns the distance between two points.
    To get the distance between two points:
        1. Get the difference between the two x-coordinates
        2. Get the difference between the two y-coordinates
        3. Sum the previous two values
        4. Return the square root of the sum
    You may want to import the `math` library for this number.
    Parameters
    ----------
    x_1: float
        the first x-coordinate
    y_1: float
        the first y-coordinate
    x_2: float
        the second x-coordinate
    y_2: float
        the second y-coordinate
    Returns
    -------
    float
        the distance between the two coordinates
    '''
    # Write your code below this line

import math

def distance(x_1, y_1, x_2, y_2):

    print("Distance Calculator")

    return(math.sqrt((x_1-x_2)**2) + (math.sqrt((y_1-y_2)**2)))

    x_1 = int(input("Enter x_1"))
    x_2 = int(input("Emter x_2"))
    y_1 = int(input("Enter y_1"))
    y_2 = int(input("Enter y_2"))

    d = distance(x_1,x_2,y_1,y_2)

    print(d)



def make_change(amount):
    '''Item 6.
    Make Change. 5 points.

    Return the combination of coins needed to make change for the given amount,
        which is given in centavos.
    For this item:
        1. You can return 1 peso, 25 centavos, 10 centavos, 5 centavos, and 1 centavo coins.
        2. Use the minimum number of coins possible.
    Parameters
    ----------
    amount: int
        the amount, in centavos, to make change for.
    Returns
    -------
    str
        the string representation of the change to be given.
        Format it like this:
            "1P:{amount}/25C:{amount}/10C:{amount}/5C:{amount}/1C:{amount}"
    '''
    # Write your code below this line

    def make_change(amount):

    new = []

    _1peso = amount // 100
    amount = amount % 100


    _25c = amount // 25
    amount = amount % 25


    _10c = amount // 10
    amount = amount % 10


    _5c = amount // 5
    amount = amount % 5

    _1c = amount // 1

    return f"1P:{_1peso}/25C:{_25c}/10C:{_10c}/5C:{_5c}/1C:{_1c}"

    print(make_change(143))
    print(make_change(341))
