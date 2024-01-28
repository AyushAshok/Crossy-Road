from turtle import Turtle
FONT = ("Courier", 17, "normal")
FONT1 = ("Courier", 50, "normal")



class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level=1
        self.goto(-290,260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level:{self.level}",font=FONT,align="left")

    def levelup(self):
        self.level+=1
        self.update()

    def ended(self):
        self.goto(-160,0)
        self.write(f"Game Over",font=FONT1,align="left")
