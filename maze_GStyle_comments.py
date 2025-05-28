import random
import queue 


class bcolors:
    """
    class for coloring path from source to destination
    """
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'



def is_valid_coords(current_coords, board_length):
    """
    While generating grid, checks if grid coordinates are valid.
    The function is also used in shortest path finding, to check if moving out of boundaries

    Args:
        current_coords (list): current coordinates' list to check
        board_length (int): board length

    Returns:
        bool: False if coordinates are out of range, otherwise True
    """
    if ((current_coords[0] <= 0) or (current_coords[0] >= board_length) 
        or (current_coords[1] <= 0) or (current_coords[1] >= board_length)):
        return False
        
    return True


def generate_maze(board_length):
    """
    Generate maze with DFS algorithm.

    Args:
        board_length (int): board length

    Return:
        (maze, coord) (tuple): tuple of maze (2D list) and list of coordinates of Start and End points
    """

    """
    Below array is representing the direction that will traverse while moving left, right, up, down directions
    moving 2 steps at a time in each direction skipping over walls
    """
    point_directions = [[0, 2], [2, 0], [0, -2], [-2, 0]]

    maze = [[1 for _ in range(board_length)] for _ in range(board_length)]
    stack = []
    visited = []

    """
    Since 0(th) column/row, and n-1(th) column/row, are grid frames, we start from (1,1) coordinate
    and we push it to stack and visited list
    """
    start_coords = [1, 1]
    maze[start_coords[0]][start_coords[1]] = 0

    stack.append(start_coords)
    visited.append(start_coords)
    current_coords = start_coords

    while(stack):
        """
        We assign stack last element to "start_coords" variable
        and using flag to determine valid coordinates
        """
        start_coords = stack[-1]
        flag = False        

        for _ in range(len(point_directions)):
            #iterate through "point_directions" list and randomly choose direction 
            random_pos = random.choice(point_directions)

            #move start_coordinates corresponding to random direction
            point_x = start_coords[0] + random_pos[0] 
            point_y = start_coords[1] + random_pos[1] 

            #keeping wall coordinates between previous and current cell to then remove the wall
            wall_x = start_coords[0] + int(random_pos[0]/2)
            wall_y = start_coords[1] + int(random_pos[1]/2)
            current_coords = [point_x, point_y] 

            #check if new coordinates are not exiting board and they are not in visted list
            is_valid_dir_point = is_valid_coords(current_coords, board_length)
            if(is_valid_dir_point and current_coords not in visited): 

                #we set 0 (as empty place, path) in place of newly generated coordinates in maze 
                maze[point_x][point_y] = 0
                """
                Remove wall and set blank space in place of wall coordinates
                else cell place will be isolated, even if new position is opened
                """
                maze[wall_x][wall_y] = 0

                #add valid coordinates in stack and in visited, set flag to True
                visited.append(current_coords)
                stack.append(current_coords)

                """
                set flag to true, since coordinates are valid,
                break after move, don't try other directions
                """
                flag = True
                break

        #backtrack if no valid coordinates
        if(flag == False):
            stack.pop()
            
    #setting start end end points in random places
    coord = set_points(maze, board_length)
    return (maze, coord)




def set_points(maze, board_length):
    """
    Setting random coordinates for start and end points.

    Args:
        maze (2D list): maze board
        board_length (int): board length

    Return:
        random_coords (list): random coordinates for Start and End points
    """
    coords = []
    
    #making sure that maze has at least two valid paths before placing start and end coordinates
    while(True):
        for i in range(board_length):
            for j in range(board_length):
                if(maze[i][j] == 0):
                    coords.append((i, j))
        if len(coords) > 2:
            break

    random_coords = random.sample(coords, 2)
    
    #assigning random coordinates first elements to start point and random coordinates second elements to end point
    start_x, start_y = random_coords[0][0], random_coords[0][1]
    end_x, end_y = random_coords[1][0], random_coords[1][1]
    print("random coordinates ", random_coords)

    #since maze contains 0s and 1s we assign 2 for 'S'(Start point) and 3 for 'E'(End point)
    maze[start_x][start_y] = 2
    maze[end_x][end_y] = 3

    return random_coords



def is_oposite_direction(moves):
    """
    While searching shortest path making sure that code is not going oposite direction:
    for example if going to left make sure code will not go to right after left.

    Args:
        moves (list): list of the moves 

    Return: 
        bool: True if step is opposite, otherwise False

    """
    #array for defining opposite directions
    not_allowed_moves = [("U","D"),("D","U"),("L","R"),("R","L")]

    #checking if current step and new step are opposite, so if it returns to the same place
    for i in range(len(moves) - 1):
        val = (moves[i], moves[i+1])
        #check if it returned to the same place
        if val in not_allowed_moves:
            return True
        
    return False
    


def is_valid_move(maze_and_coords, moves, board_length):
    """
    Check for valid moves

    Args:
        maze_and_coords (tuple): board (2D list) and list of coordinates of Start and End points
        moves (list): list of the moves
        board_length (int): board length

    Return:
        bool: check if new step coordinates are not valid False, otherwise True
    """
    maze, coords = maze_and_coords
    start_x = coords[0][0]
    start_y = coords[0][1]

    """
    since our start location is fixed, 
    we are iterating through all the directions and changing start location based on current direction
    """
    for move in moves:
        if move == "L":
            start_y = start_y - 1
        elif move == "R":
            start_y = start_y + 1
        elif move == "U":
            start_x = start_x - 1
        elif move == "D":
            start_x = start_x + 1

    #check if new path coordinates are not exiting board boundaries
    if is_valid_coords([start_x, start_y], board_length)==False:
        return False
    
    #check if current coordinates place is not wall
    if maze[start_x][start_y] == 1:
        return False
    
    #prevents from returnining to the same place
    if is_oposite_direction(moves):
        return False

    return True



def is_endpoint(maze_and_coords, moves):
    """
    Check if path has reached to end point

    Args:
        maze_and_coords (tuple): board (2D list) and list of coordinates of Start and End points
        moves (list): list of the moves

    Return:
        bool: if we reached to the endpoint True, else False
    """
    maze, coords = maze_and_coords
    start_x = coords[0][0]
    start_y = coords[0][1]

    end = (coords[1][0],coords[1][1])
    #we are iterating through all the directions and changing start location based on current direction
    for move in moves:
        if move == "L":
            start_y = start_y - 1
        elif move == "R":
            start_y = start_y + 1
        elif move == "U":
            start_x = start_x - 1
        elif move == "D":
            start_x = start_x + 1

    #checks if we have reached to the end point
    if ((start_x, start_y)) == end:
        return True
    
    return False



def find_shortest_path(maze_and_coords, board_length):
    """
    Find shortest path with BFS algorithm

    Args:
        maze_and_coords (tuple): board (2D list) and list of coordinates of Start and End points
        board_length (int): board length

    Return:
        prev_dir (string): valid moves

    """

    #declaring queue for adding moves 
    q_moves = queue.Queue()
    q_moves.put("")
    prev_dir = ""

    while not is_endpoint(maze_and_coords, prev_dir):
        #getting first element(direction) in queue
        prev_dir = q_moves.get()

        #iterating through all possible directions
        for dir in ["L", "R", "U", "D"]:
            #adding new direction to the previous directions
            current_dir = prev_dir + dir
            
            #before adding to the queue, check if move is valid
            if is_valid_move(maze_and_coords, current_dir, board_length):
                q_moves.put(current_dir)

    return prev_dir

    

def add_path_to_maze(maze_and_coords, path):
    """
    Adding placeholder "4" in maze board that will represent shortest path

    Args:
        maze_and_coords (tuple): board (2D list) and list of coordinates of Start and End points
        path (string): path between Start and End points

    Return:
        maze (2D list): board with highlighted with points' path
    """
    maze, coords = maze_and_coords
    start_x, start_y = coords[0][0], coords[0][1]

    for direction in path[:-1]:
        if direction == "L":
            start_y = start_y - 1
            maze[start_x][start_y] = 4
        elif direction == "R":
            start_y = start_y + 1
            maze[start_x][start_y] = 4
        elif direction == "U":
            start_x = start_x - 1
            maze[start_x][start_y] = 4
        elif direction == "D":
            start_x = start_x + 1
            maze[start_x][start_y] = 4

    return maze



def print_maze(maze_and_coords, path):
    """
    Replacing walls, shortest path, empty spaces and start/end points while printing maze

    Args:
        maze_and_coords (tuple): board (2D list) and list of coordinates of Start and End points
        path (string): path from Start to End point
    """
    maze = add_path_to_maze(maze_and_coords, path)
    for row in maze:
        row = "".join(map(str, row))
        row = row.replace("1","#")\
        .replace("2", "S")\
        .replace("3", "E")\
        .replace("0", " ")\
        .replace("4", bcolors.RED + "." + bcolors.ENDC)
        print(row)




def main():
    #making sure user input is in valid range and size is odd number 
    while True:
        board_length = int(input("Enter odd number for the size of the grid: "))
        try:
            board_length = int(board_length)
        except ValueError:
            print("Please enter Valid number")
            continue
        if ((5 <= board_length <= 100) and (board_length % 2 == 1)):
            break
        else:
            print("Please enter valid range: 5-100 and odd number")

    
    maze = generate_maze(board_length)
    shortest_path = find_shortest_path(maze, board_length)
    print_maze(maze, shortest_path)

    if shortest_path:
        print(f"\nPath length: {len(shortest_path)}")
    else:
        print("No path found.")

    


if __name__=="__main__":
    main()
