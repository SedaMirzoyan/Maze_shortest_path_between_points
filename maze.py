import random
import queue 

class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'


def get_size(n):
    #board_length = (n * 2) + 1
    board_length = n
    return board_length 


def is_valid_coords(current_coords, board_length):
    if ((current_coords[0] <= 0) or (current_coords[0] >= board_length) 
        or (current_coords[1] <= 0) or (current_coords[1] >= board_length)):
        return False
        
    return True


def generate_maze(board_length):
    point_directions = [[0, 2], [2, 0], [0, -2], [-2, 0]]
    maze = [[1 for _ in range(board_length)] for _ in range(board_length)]
    stack = []
    visited = []

    start_coords = [1, 1]
    maze[start_coords[0]][start_coords[1]] = 0
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

            is_valid_dir_point = is_valid_coords(current_coords, board_length)
            if(is_valid_dir_point and current_coords not in visited): 
                maze[point_x][point_y] = 0
                maze[wall_x][wall_y] = 0
                visited.append(current_coords)
                stack.append(current_coords)
                flag = True
                break

        if(flag == False):
            stack.pop()
            
    coord = set_points(maze, board_length)
    return (maze, coord)



def set_points(maze, board_length):
    coords = []
            
    while(True):
        for i in range(board_length):
            for j in range(board_length):
                if(maze[i][j] == 0):
                    coords.append((i, j))
        if len(coords) > 2:
            break

    random_coords = random.sample(coords, 2)
    
    start_x, start_y = random_coords[0][0], random_coords[0][1]
    end_x, end_y = random_coords[1][0], random_coords[1][1]
    print("rc ", random_coords)
    maze[start_x][start_y] = 2
    maze[end_x][end_y] = 3

    return random_coords


    
def is_valid_move(maze_and_coords, moves, board_length):
    maze, coords = maze_and_coords
    start_x = coords[0][0]
    start_y = coords[0][1]

    for move in moves:
        if move == "L":
            start_y = start_y - 1
        elif move == "R":
            start_y = start_y + 1
        elif move == "U":
            start_x = start_x - 1
        elif move == "D":
            start_x = start_x + 1

    if  is_valid_coords([start_x, start_y], board_length)==False:
        return False
    if maze[start_x][start_y] == 1:
        return False
    
    return True



def is_endpoint(maze_and_coords, moves):
    maze, coords = maze_and_coords
    start_x = coords[0][0]
    start_y = coords[0][1]

    end = (coords[1][0],coords[1][1])
    for move in moves:
        
        if move == "L":
            start_y = start_y - 1
        elif move == "R":
            start_y = start_y + 1
        elif move == "U":
            start_x = start_x - 1
        elif move == "D":
            start_x = start_x + 1

    if ((start_x, start_y)) == end:
        return True
    
    return False


def find_shortest_path(maze_and_coords, board_length):
    q_moves = queue.Queue()
    q_moves.put("")
    direction = ""
    
    while not is_endpoint(maze_and_coords, direction):
        direction = q_moves.get()
        for prev_dir in ["L", "R", "U", "D"]:
            current_dir = direction + prev_dir
            
            if is_valid_move(maze_and_coords, current_dir, board_length):
                q_moves.put(current_dir)

    return direction

    

def add_path_to_maze(maze_and_coords, path):
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
    maze = add_path_to_maze(maze_and_coords, path)
    for row in maze:
        row = "".join(map(str, row))
        row = row.replace("1","#")\
        .replace("2", "S")\
        .replace("3", "E")\
        .replace("0"," ")\
        .replace("4", bcolors.RED + "." + bcolors.ENDC)

        print(row)


def main():
    while True:
        n = int(input("Enter odd number for the size of the grid: "))
        try:
            n = int(n)
        except ValueError:
            print("Please enter Valid number")
            continue
        if ((5 <= n <= 13) and (n % 2 == 1)):
            break
        else:
            print("Please enter valid range: 5-13 and odd number")

    
    board_length = get_size(n)
    maze = generate_maze(board_length)
    shortest_path = find_shortest_path(maze, board_length)
    print_maze(maze, shortest_path)

    if shortest_path:
        print(f"\nPath length: {len(shortest_path)}")
    else:
        print("No path found.")

    


if __name__=="__main__":
    main()