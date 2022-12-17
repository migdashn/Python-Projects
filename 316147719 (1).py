import numpy as np
import matplotlib.pyplot as plt
import game_of_life_interface

class GameOfLife(game_of_life_interface.GameOfLife):
    def __init__(self, size_of_board, board_start_mode, rules, rle, pattern_position):
        self.size_of_board = size_of_board
        self.board_start_mode = board_start_mode
        self.rules = rules
        self.rle = rle
        self.pattern_position = pattern_position
        self.grid = [[0 for i in range(self.size_of_board)] for j in range(self.size_of_board)]
        self.alive = 255
        self.dead = 0
        self.vals = [self.alive, self.dead]
        self.starting_position()

    def update(self):
        self.new_grid = tuple(tuple(self.grid[i][j] for j in range(self.size_of_board)) for i in range(self.size_of_board))
        r = [tuple(int(num) for num in self.rules.split("/")[0] if num.isdigit()),  #list with 2 tuples of the rules with only numbler
            tuple(int(num) for num in self.rules.split("/")[1] if num.isdigit())]

        for i in range(self.size_of_board):
            for j in range(self.size_of_board):
                alives = int((self.new_grid[(i - 1)%self.size_of_board][(j - 1)%self.size_of_board]+self.new_grid[(i - 1)%self.size_of_board][j]+
                              self.new_grid[(i - 1)%self.size_of_board][(j + 1)%self.size_of_board]+self.new_grid[i][(j - 1)%self.size_of_board]+self.new_grid[i][(j + 1)%self.size_of_board]+
                              self.new_grid[(i + 1)%self.size_of_board][(j - 1)%self.size_of_board]+self.new_grid[(i + 1)%self.size_of_board][j]+
                              self.new_grid[(i + 1)%self.size_of_board][(j + 1)%self.size_of_board])/255)

                if self.new_grid[i][j] == self.dead:
                    for k in range(len(r[0])):
                        if alives == r[0][k]:
                            self.grid[i][j] = self.alive
                            break

                elif self.new_grid[i][j] == self.alive:    #if the cell alive - kill him and bringing him back alive if he stand by the rules
                    self.grid[i][j] = self.dead
                    for k in range(0, len(r[1])):
                        if alives == r[1][k]:
                            self.grid[i][j] = self.alive
                            break


    def save_board_to_file(self, file_name):
        return plt.imsave(file_name, self.grid)

    def display_board(self):
        plt.imshow(self.grid)
        plt.pause()

    def return_board(self):
        return self.grid


    def transform_rle_to_matrix(self, rle):
        y = self.pattern_position[0]
        x = self.pattern_position[1]
        for i in rle:
            if i != '!':       #running intil !
                if i != '$':
                    if i.isalpha():
                        scalar_index = rle.index(i)
                        rle = rle.replace(i, 'x', 1)
                        if rle[scalar_index - 1].isdigit():
                            scalar = rle[scalar_index - 1]          #checking the last 2 char in the rle to find the scalar and replcaing ani char with x to prevent confusion
                            if rle[scalar_index - 2].isdigit():
                                scalar = rle[scalar_index - 2] + scalar
                        else:
                                scalar = 1
                        if i == 'b':
                            for j in range(x, x + int(scalar)):
                                self.grid[y][j] = self.dead
                            x += int(scalar)
                        elif i == 'o':
                            for j in range(x, x + int(scalar)):
                                self.grid[y][j] = self.alive
                            x += int(scalar)
                else:
                    scalar = ''
                    scalar_index = rle.index(i)
                    rle = rle.replace(i, 'x', 1)
                    if rle[scalar_index - 1].isdigit():
                        scalar = rle[scalar_index - 1]
                        if rle[scalar_index - 2].isdigit():
                            scalar = rle[scalar_index - 2] + scalar
                    if scalar == '':
                        y += 1
                        x = self.pattern_position[1]
                    else:
                        y += int(scalar)
                        x = self.pattern_position[1]
        return self.grid


    def starting_position(self):
        if (self.rle == "" and self.board_start_mode == 1) or (self.rle == '' and self.board_start_mode != 1 and self.board_start_mode != 2 and self.board_start_mode != 3 and self.board_start_mode != 4):
            self.grid = np.random.choice(self.vals , size=(self.size_of_board*self.size_of_board),p=[0.5 ,0.5]).reshape(self.size_of_board, self.size_of_board).tolist()
        elif self.rle == "" and self.board_start_mode == 2:
            self.grid = np.random.choice(self.vals, size=(self.size_of_board * self.size_of_board), p=[0.8, 0.2]).reshape(self.size_of_board, self.size_of_board).tolist()
        elif self.rle == "" and self.board_start_mode == 3:
            self.grid = np.random.choice(self.vals, size=(self.size_of_board * self.size_of_board), p=[0.2, 0.8]).reshape(self.size_of_board, self.size_of_board).tolist()
        elif self.rle == "" and self.board_start_mode == 4:
            self.pattern_position = (10, 10)
            self.transform_rle_to_matrix("24bo$22bobo$12b2o6b2o12b2o$11bo3bo4b2o12b2o$2o8bo5bo3b2o$2o8bo3bob2o4bobo$10bo5bo7bo$11bo3bo$12b2o!")
        else:
            self.transform_rle_to_matrix(self.rle)


if __name__ == '__main__':
    print('put your tests here')
    GameOfLife()