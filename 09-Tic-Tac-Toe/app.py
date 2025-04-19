"""
Tic-Tac-Toe Game
Created by: Touseef
Date: April 2, 2025
Special Features: Friendly messages and personalized design
"""

import tkinter as tk
import numpy as np

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe - By Touseef")
        self.canvas = tk.Canvas(self.window, width=300, height=350, bg='lightblue')
        self.canvas.pack()
        
        self.board = np.zeros((3,3))
        self.player_turn = 1
        self.scores = {1: 0, -1: 0, 'tie': 0}
        
        self.initialize_board()
        self.canvas.bind("<Button-1>", self.click)
        
        self.window.mainloop()

    def initialize_board(self):
        self.canvas.delete("all")
        for i in range(1,3):
            self.canvas.create_line(0, i*100, 300, i*100, width=3)
            self.canvas.create_line(i*100, 0, i*100, 300, width=3)
        self.board = np.zeros((3,3))
        self.player_turn = 1
        self.canvas.create_text(150, 325, text=f"Score - X: {self.scores[1]}  O: {self.scores[-1]}  Tie: {self.scores['tie']}", font=("Arial", 12))

    def draw_X(self, row, col):
        x1, y1 = col * 100 + 20, row * 100 + 20
        x2, y2 = (col+1) * 100 - 20, (row+1) * 100 - 20
        self.canvas.create_line(x1, y1, x2, y2, width=3, fill='darkred')
        self.canvas.create_line(x1, y2, x2, y1, width=3, fill='darkred')

    def draw_O(self, row, col):
        x, y = col * 100 + 50, row * 100 + 50
        self.canvas.create_oval(x-30, y-30, x+30, y+30, width=3, outline='darkgreen')

    def is_winner(self, player):
        for i in range(3):
            if sum(self.board[i,:]) == player*3 or sum(self.board[:,i]) == player*3:
                return True
        if sum([self.board[i,i] for i in range(3)]) == player*3 or sum([self.board[i,2-i] for i in range(3)]) == player*3:
            return True
        return False

    def is_tie(self):
        return not np.any(self.board == 0)

    def display_gameover(self, result):
        message = ""
        if result == 1:
            message = "Player X (Touseef ki taraf se Mubarak Ho!) jeet gaya!"
        elif result == -1:
            message = "Player O jeet gaya! Next time try karo!"
        else:
            message = "Yeh match tie ho gaya! Dono ache khele!"

        self.scores[result if result in [1, -1] else 'tie'] += 1
        self.canvas.create_rectangle(20, 120, 280, 180, fill='white', outline='black')
        self.canvas.create_text(150, 150, text=message, font=("Arial", 12, "bold"))
        self.canvas.create_text(150, 200, text="Phir se khelne ke liye kisi bhi jaga click karein.", font=("Arial", 10))

    def click(self, event):
        if np.any(self.board == 0):
            row, col = event.y // 100, event.x // 100
            if row < 3 and self.board[row, col] == 0:
                if self.player_turn == 1:
                    self.draw_X(row, col)
                    self.board[row, col] = 1
                else:
                    self.draw_O(row, col)
                    self.board[row, col] = -1

                if self.is_winner(self.player_turn):
                    self.display_gameover(self.player_turn)
                    self.player_turn = 1
                    return
                elif self.is_tie():
                    self.display_gameover(0)
                    self.player_turn = 1
                    return

                self.player_turn *= -1
        else:
            self.initialize_board()

if __name__ == "__main__":
    TicTacToe()
