import random

#board_length = (n * 2) + 1
board_length = 9

class Maze:
    def __init__(self):
        #self.m_board = [['#' for _ in range(board_length-1)] for _ in range(board_length-1)]
        self.directions = [[0, 2], [2, 0], [0, -2], [-2, 0]]
            
        self.e_x_coord = random.randint(0, board_length-1)
        self.e_y_coord = random.randint(0, board_length-1)
        self.s_x_coord, self.s_y_coord = 0, 0
    
        while (self.e_x_coord == self.s_x_coord):
            self.s_x_coord = random.randint(0, board_length-1)

        while (self.e_y_coord == self.s_y_coord):
            self.s_y_coord = random.randint(0, board_length-1)

        #self.m_board[self.e_x_coord][self.e_y_coord] = 'E'
        #self.m_board[self.s_x_coord][self.s_y_coord] = 'S'

    '''
    def print_board(self):
        for i in range(m_board_length):
            for j in range(m_board_width):
                if(((i == 0 or i == m_board_length-1)) or (j == 0 or j == m_board_width-1)):
                    print('#', end='')
                else:
                    print(" ", end="")
            print("")
    '''

    def is_valid(self, start_coords, dir):
        if ((start_coords[0] + dir[0] < 0) or (start_coords[0] + dir[0] > board_length) 
            or (start_coords[1] + dir[1] < 0) or (start_coords[1] + dir[1] > board_length)):
            return False
        
        return True



    def generate_maze(self, n):
        maze = [[1 for _ in range(board_length)] for _ in range(board_length)]
        #print(maze)
        visited = []
        stack = []
        start_coords = [1, 1]
        stack.append(start_coords)
        visited.append(start_coords)
        #random_index = random.randint(0, 3)
        #dir = self.directions[random_index]
        current_coords = [1, 1]


        #while((stack) and len(visited) > n * n):
        while(stack):
            random_index = random.randint(0, 3)
            dir = self.directions[random_index]
            is_valid_direction = self.is_valid(start_coords, dir)
            print("is_valid_direction ", is_valid_direction)
            if(is_valid_direction):
                current_coords[0] = start_coords[0] + dir[0] 
                current_coords[1] = start_coords[1] + dir[1] 
                print("current_coords ", start_coords)
                if current_coords not in visited:
                    visited.append(current_coords)
                else:
                    stack.pop()
                start_coords = current_coords
                print("start_coords ", start_coords)
            print("len visited ", len(visited))

                    

        return maze
    

    def print_board(self):
        maze = self.generate_maze()
        for i in range(board_length):
            for j in range(board_length):
                print(maze[i][j], end = " ")
            print("\n")





    def find_shortest_path(self):
        pass

    

def main():
 
    n = 4
    ob = Maze()
    #ob.print_board()
    ob.generate_maze(n)
    #ob.print_board()
    


if __name__=="__main__":
    main()