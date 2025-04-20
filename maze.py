import random


def get_size(n):
    board_length = (n * 2) + 1
    return board_length 

 
def is_valid_coords(start_coords, dir, board_length):
    if ((start_coords[0] + dir[0] < 0) or (start_coords[0] + dir[0] >= board_length) 
        or (start_coords[1] + dir[1] < 0) or (start_coords[1] + dir[1] >= board_length)):
        print("Out of range")
        return False
        
    return True


def generate_maze(board_length):
    directions = [[0, 2], [2, 0], [0, -2], [-2, 0]]
    maze = [[1 for _ in range(board_length)] for _ in range(board_length)]
    stack = []
    visited = []

    start_coords = [1, 1]
    maze[1][1] = 0
    stack.append(start_coords)
    print("stackhhhhhhhhhhhh ", stack)
    visited.append(start_coords)
    #random_index = random.randint(0, 3)
    #dir = self.directions[random_index]
    current_coords = start_coords

    #while((stack) and len(visited) > n * n):
    while(stack):
        random_index = random.randint(0, 3)
        print("random_index ", random_index)
        dir = directions[random_index]
        print("dir ", dir)
        is_valid_direction = is_valid_coords(start_coords, dir, board_length)
        print("is_valid_direction ", is_valid_direction)
        if(is_valid_direction):
            #start_coords = stack.pop()
            px = start_coords[0] + dir[0] 
            py = start_coords[1] + dir[1] 
            current_coords = [px, py]
            #print("current_coords ", current_coords)
            if current_coords not in visited:
                visited.append(current_coords)
                stack.append(current_coords)
                maze[px][py] = 0
                start_coords = current_coords
            else:
                #start_coords = stack.pop()
                stack.pop()
            #start_coords = current_coords
            #print("start_coords ", start_coords)
        print("visited ", visited)
        print("stack ", stack)
                    

    return maze
    

def print_board(board_length):
    maze = generate_maze(board_length)
    for i in range(board_length):
        for j in range(board_length):
            print(maze[i][j], end = " ")
        print("\n")





def find_shortest_path():
    pass

    

def main():
 
    n = 4
    board_length = get_size(n)
    generate_maze(board_length)
    print_board(board_length)
    


if __name__=="__main__":
    main()