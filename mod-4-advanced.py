#!/usr/bin/env python
# coding: utf-8

# In[38]:


'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph = {
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
}):
    
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
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
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        return "friends"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    else:
        return "no relationship"
    
print(relationship_status("@joaquin", "@chums"))
print(relationship_status("@chums", "@joeilagan"))
print(relationship_status("@bongolpoc", "@joeilagan"))


# In[39]:


def tic_tac_toe(board1=None, board2=None, board3=None, board4=None, board5=None, board6=None, board7=None):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
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
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    boards = {
        'board1': board1,
        'board2': board2,
        'board3': board3,
        'board4': board4,
        'board5': board5,
        'board6': board6,
        'board7': board7,
    }

    winners = {}

    for board_name, board in boards.items():
        if board is None:
            continue

        grid = len(board)
        row = 0
        column = 0

        for a in board:
            sumset_horizontal = set(board[row])
            if len(sumset_horizontal) == 1 and '' not in sumset_horizontal:
                winners[board_name] = sumset_horizontal.pop()
                break
            row += 1

        if winners.get(board_name):
            continue

        if len(set([board[x][x] for x in range(grid)])) == 1 and board[0][0] != '':
            winners[board_name] = set([board[x][x] for x in range(grid)]).pop()

        if winners.get(board_name):
            continue

        if len(set([board[grid - 1 - y][y] for y in range(grid)])) == 1 and board[grid - 1][0] != '':
            winners[board_name] = set([board[y][y] for y in range(grid)]).pop()

        vertical_board = [z for z in zip(*board)]

        for b in board:
            sumset_vertical = set(vertical_board[column])
            if len(sumset_vertical) == 1 and '' not in sumset_vertical:
                winners[board_name] = sumset_vertical.pop()
                break
            column += 1

        if winners.get(board_name):
            continue

        winners[board_name] = "NO WINNER"

    return winners

result = tic_tac_toe(board1=[
    ['X', 'X', 'O'],
    ['O', 'X', 'O'],
    ['O', '', 'X'],
], board2=[
    ['X', 'X', 'O'],
    ['O', 'X', 'O'],
    ['', 'O', 'X'],
], board3=[
    ['O', 'X', 'O'],
    ['', 'O', 'X'],
    ['X', 'X', 'O'],
], board4=[
    ['X', 'X', 'X'],
    ['O', 'X', 'O'],
    ['O', '', 'O'],
], board5=[
    ['X', 'X', 'O'],
    ['O', 'X', 'O'],
    ['X', '', 'O'],
], board6=[
    ['X', 'X', 'O'],
    ['O', 'X', 'O'],
    ['X', '', ''],
], board7=[
    ['X', 'X', 'O', ''],
    ['O', 'X', 'O', 'O'],
    ['X', '', '', 'O'],
    ['O', 'X', '', '']
])
print(result)


# In[42]:


def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
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
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    legs = {
    ("upd", "admu"): {"travel_time_mins": 10},
    ("admu", "dlsu"): {"travel_time_mins": 35},
    ("dlsu", "upd"): {"travel_time_mins": 55}
}
    legs = list(route_map.keys())
    count = len(legs)
    a = 0
    while a < count:
        if (str(first_stop), legs[a][1]) in legs:
            travel_time = route_map[(first_stop, legs[a][1])]["travel_time_mins"]
            return travel_time
        a += 1
    
    b = (a + 1) % count
    c = 0
    while c < count:
        if (legs[b][0], second_stop) in route_map.keys():
            travel_time += route_map[(legs[b])]["travel_time_mins"]
            return travel_time
        else:
            travel_time += route_map[(legs[b])]["travel_time_mins"]
        b += 1
        c += 1

result = eta(first_stop="upd", second_stop="dlsu", route_map=legs)
print("Total Travel Time to Next Stop: " + str(result) + " minutes" )


# In[ ]:





# In[ ]:





# In[ ]:




