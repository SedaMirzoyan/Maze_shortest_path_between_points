import random


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
            print("is_valid_direction ", is_valid_dir_point, current_coords)
            if(is_valid_dir_point and current_coords not in visited): 
                maze[point_y][point_x] = 0
                maze[wall_y][wall_x] = 0

                visited.append(current_coords)
                stack.append(current_coords)
                flag = True
                print("visited ", visited)
                print("stack ", stack)
                break

            print(" current_coords ", current_coords, "wall_coords ", wall_coords)

        if(flag == False):
            stack.pop()
            
        print("visited ", visited)
        print("stack ", stack)
        
    return maze
    


def print_maze(board_length):       
    maze = generate_maze(board_length)
    for row in maze:
        print("".join('#' if cell else ' ' for cell in row))




def find_shortest_path():
    pass

    

def main():
 
    n = 4
    board_length = get_size(n)
    generate_maze(board_length)
    print_maze(board_length)
    


if __name__=="__main__":
    main()