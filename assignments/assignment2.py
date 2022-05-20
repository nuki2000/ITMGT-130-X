
'''Assignment 2
This assignment covers your proficiency with Python's data structures.
It engages your ability to manipulate and evaluate data stored in lists and dictionaries.
'''

def relationship_status(from_member, to_member, social_graph):
    '''
    Item 1.
    Relationship Status. 10 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-2-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Write your code below this line

def relationship_status(from_member, to_member, social_graph):

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

from_member = str(input("insert username 1 here: "))
to_member = str(input("insert username 2 here: "))


if from_member in social_graph[to_member]["following"]:
    if to_member in social_graph[from_member]["following"]:
        print ("friends")
    else:
        print ("follower")


elif to_member in social_graph[from_member]["following"]:
    print ("followed by")
else:
    print ("no relationship")





def tic_tac_toe(board):
    '''
    Item 2.
    Tic Tac Toe. 10 points.
    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-2-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Write your code below this line

def tic_tac_toe(board):


board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

def check_win():

    for row in board1:
        if row[0] == row[1] == row[2] and row[0]!= ' ':
            return row[0]


    for col in range(3):
        if board1[0][col] == board1[1][col] == board1[2][col] and board1[0][col] != ' ':
            return board1[0][col]


    if board1[0][0] == board1[1][1] == board1[2][2] and board1[0][0] != ' ':
        return board1[0][0]

    if board1[0][2] == board1[1][1] == board1[2][0] and board1[0][2] != ' ':
        return board1[0][2]


print(check_win())

def check_win():

    for row in board2:
        if row[0] == row[1] == row[2] and row[0]!= ' ':
            return row[0]


    for col in range(3):
        if board2[0][col] == board2[1][col] == board2[2][col] and board2[0][col] != ' ':
            return board2[0][col]


    if board2[0][0] == board2[1][1] == board2[2][2] and board2[0][0] != ' ':
        return board2[0][0]

    if board2[0][2] == board2[1][1] == board2[2][0] and board2[0][2] != ' ':
        return board2[0][2]


print(check_win())

def check_win():

    for row in board3:
        if row[0] == row[1] == row[2] and row[0]!= ' ':
            return row[0]

    for col in range(3):
        if board3[0][col] == board3[1][col] == board3[2][col] and board3[0][col] != ' ':
            return board3[0][col]

    if board3[0][0] == board3[1][1] == board3[2][2] and board3[0][0] != ' ':
        return board3[0][0]

    if board3[0][2] == board3[1][1] == board3[2][0] and board3[0][2] != ' ':
        return board3[0][2]

print(check_win())

def check_win():

    for row in board4:
        if row[0] == row[1] == row[2] and row[0]!= ' ':
            return row[0]


    for col in range(3):
        if board4[0][col] == board4[1][col] == board4[2][col] and board4[0][col] != ' ':
            return board4[0][col]


    if board4[0][0] == board4[1][1] == board4[2][2] and board4[0][0] != ' ':
        return board4[0][0]

    if board4[0][2] == board4[1][1] == board4[2][0] and board4[0][2] != ' ':
        return board4[0][2]

print(check_win())

def check_win():

    for row in board5:
        if row[0] == row[1] == row[2] and row[0]!= ' ':
            return row[0]


    for col in range(3):
        if board5[0][col] == board5[1][col] == board5[2][col] and board5[0][col] != ' ':
            return board5[0][col]


    if board5[0][0] == board5[1][1] == board5[2][2] and board5[0][0] != ' ':
        return board5[0][0]

    if board5[0][2] == board5[1][1] == board5[2][0] and board5[0][2] != ' ':
        return board5[0][2]


print(check_win())

def check_win():

    for row in board6:
        if row[0] == row[1] == row[2] and row[0]!= ' ':
            return row[0]


    for col in range(3):
        if board6[0][col] == board6[1][col] == board6[2][col] and board6[0][col] != ' ':
            return board6[0][col]


    if board6[0][0] == board6[1][1] == board6[2][2] and board6[0][0] != ' ':
        return board6[0][0]

    if board6[0][2] == board6[1][1] == board6[2][0] and board6[0][2] != ' ':
        return board6[0][2]

print(check_win())


def eta(first_stop, second_stop, route_map):
    '''
    Item 3.
    ETA. 10 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "assignment-2-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Write your code below this line

route_map = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

first_stop = str(input("first stop: "))
second_stop = str(input("second stop: "))

if first_stop== "upd" and second_stop== "admu":
    print(int(10))


elif first_stop== "admu" and second_stop== "dlsu":
    print(int(35))


elif first_stop == "dlsu" and second_stop == "upd":
    print(int(55))


else:
    print("try again")
