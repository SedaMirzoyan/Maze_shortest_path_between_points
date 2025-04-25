import random
import queue 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_size(n):
    board_length = (n * 2) + 1
    return board_length 


def is_valid_coords(current_coords, board_length):
    if ((current_coords[0] <= 0) or (current_coords[0] >= board_length) 
        or (current_coords[1] <= 0) or (current_coords[1] >= board_length)):
        print("Out of range")
        return False
        
    return True


def generate_maze(board_length):
    point_directions = [[0, 2], [2, 0], [0, -2], [-2, 0]]
    maze = [[1 for _ in range(board_length)] for _ in range(board_length)]
    stack = []
    visited = []

    start_coords = [1, 1]
    maze[start_coords[1]][start_coords[0]] = 0
    stack.append(start_coords)
    visited.append(start_coords)
    current_coords = start_coords

    while(stack):
        start_coords = stack[-1]
        flag = False        

        for _ in range(len(point_directions)):
            random_pos = random.choice(point_directions)
            point_x = start_coords[0] + random_pos[0] 
            point_y = start_coords[1] + random_pos[1] 
            wall_x = start_coords[0] + int(random_pos[0]/2)
            wall_y = start_coords[1] + int(random_pos[1]/2)
            current_coords = [point_x, point_y] 
            wall_coords = [wall_x, wall_y]

            is_valid_dir_point = is_valid_coords(current_coords, board_length)
            if(is_valid_dir_point and current_coords not in visited): 
                maze[point_y][point_x] = 0
                maze[wall_y][wall_x] = 0

                visited.append(current_coords)
                stack.append(current_coords)
                flag = True
                break

        if(flag == False):
            stack.pop()
            
    coord = set_letters(maze, board_length)
        
    return (maze, coord)


def set_letters(maze, board_length):
    coords = []
    for i in range(board_length):
        for j in range(board_length):
            if(maze[i][j] == 0):
                coords.append((i, j))
        
    random_coord = random.sample(coords, 2)
    start_x, start_y = random_coord[0][0], random_coord[0][1]
    end_x, end_y = random_coord[1][0], random_coord[1][1]
    print("rc ", random_coord)
    maze[start_y][start_x] = 2
    #maze[start_y][start_x] = 'S'
    maze[end_y][end_x] = 3
    #maze[end_y][end_x] = 'E'

    return random_coord


    
def is_valid_move(maze_and_coords, moves, board_length):
    maze, coords = maze_and_coords
    start_y = coords[0][0]
    start_x = coords[0][1]

    for move in moves.split():
        if move == "Left":
            start_x = start_x - 1
        elif move == "Right":
            start_x = start_x + 1
        elif move == "Up":
            start_y = start_y - 1
        elif move == "Down":
            start_y = start_y + 1

    if  is_valid_coords([start_y, start_x], board_length)==False:
        return False
    print("start_y",start_y)
    print("start_x",start_x)
    print(maze[start_x][start_y])
    if maze[start_y][start_x] == 1:
        return False
    
    return True

def is_endpoint(maze_and_coords, moves):
    maze, coords = maze_and_coords
    start_y = coords[0][0]
    start_x = coords[0][1]

    end = (coords[1][0],coords[1][1])
    for move in moves.split():
        
        if move == "Left":
            start_x = start_x - 1
        elif move == "Right":
            start_x = start_x + 1
        elif move == "Up":
            start_y = start_y - 1
        elif move == "Down":
            start_y = start_y + 1

    if ((start_y, start_x)) == end:
        return False
    
    return True


def find_shortest_path(maze_and_coords, board_length):
    maze, coords = maze_and_coords
    
    start_y, start_x = coords[0][0], coords[0][1]
    end_y, end_x = coords[1][0], coords[1][1]
    print(start_y, start_x)
    print("~~~~~~",  maze)
    print("maze[start_y][start_x] = ", maze[start_x][start_y])

    q_moves = queue.Queue()
    q_moves.put("")
    direction = ""
    
    #counter = 0
    while is_endpoint(maze_and_coords, direction):
        direction = q_moves.get()
        print("~!!!!!!!!", direction)
        for prev_dir in ["Left", "Right", "Up", "Down"]:
            current_dir = direction + " " + prev_dir
            
            if is_valid_move(maze_and_coords, current_dir, board_length):
                q_moves.put(current_dir)

        #counter += 1
        #if counter >= 30:
        #    break

    



def print_maze(maze_and_coords):      
    maze, coords = maze_and_coords
    for row in maze:
        print("".join('#' if cell == 1 
                      else 'S' if cell == 2 #'S' #2 
                      else 'E' if cell == 3 #'E' #3 
                      else  bcolors.FAIL + '.' + bcolors.ENDC if cell == 4 
                      else  ' ' for cell in row))




def main():
    n = 4
    #n = int(input("Enter size of the grid"))
    board_length = get_size(n)
    maze = generate_maze(board_length)
    path = find_shortest_path(maze, board_length)
    print_maze(maze)

    if path:
        print(f"\nPath length: {len(path)}")
    else:
        print("No path found.")

    


if __name__=="__main__":
    main()