from tkinter import * 
from tkinter import messagebox
import time 
import random 

window = Tk()
window.title("Pong Game!")
window.resizable(0,0)
window.wm_attributes("-topmost", 1) #makes it so that this window is always on top of any others

canvas = Canvas(window, width = 600, height = 500, bg = "black", bd = 1, highlightthickness = 1)
canvas.grid(row = 1, column = 1)
canvas.create_line(300, 0, 300, 500, fill = "white")
score_label = canvas.create_text(300, 30, font = ("times", 40), text = "0 : 0", fill = "white")
window.update()


class Ball:

    def __init__(self, canvas, paddle1, paddle2, color):
        self.canvas = canvas
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.color = color
        self.id = canvas.create_oval(10,10, 30,30 , fill = self.color)
        self.canvas.move(self.id, 300, 300)
        starts = [-3,-2, -1 , 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[1]
        self.y = starts[2]
        self.score1 = 0 
        self.score2 = 0 
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

    def draw_ball(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 4
        if pos[3] >= self.canvas_height:
            self.y = -4
        if pos[0] <= 0:
            self.score2 += 1
            self.x = 4
            canvas.itemconfigure(score_label, text = str(self.score1) + " : " + str(self.score2))
        if pos[2] >= self.canvas_width:
            self.x = -4
            self.score1 += 1
            canvas.itemconfigure(score_label, text = str(self.score1) + " : " + str(self.score2))
        
        if self.hit_paddle1(pos):
            self.x = 4
        if self.hit_paddle2(pos):
            self.x = -4

    
    def hit_paddle1(self, pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                return True
            return False
        
    def hit_paddle2(self, pos):
        paddle_pos = self.canvas.coords(self.paddle2.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                return True
            return False
    
class Paddle1():

    pos = [0,0,0,0]

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.id = self.canvas.create_rectangle(10,180,25, 280, fill = self.color)
        self.y = 0 
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind_all("w", self.move_up)
        self.canvas.bind_all("s", self.move_down)
    
    def move_up(self, event):
        self.y = -4

    def move_down(self, event):
        self.y = 4
    
    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= self.canvas_height:
            self.y = 0 

class Paddle2():

    pos = [0,0,0,0]

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.id = self.canvas_rectangle(575, 180, 590, 280, fill = self.color)
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind_all("<KeyPress-Up>", self.move_up)
        self.canvas.bind_all("<KeyPress-Down>", self.move_down)
        


            
            
            
window.mainloop()