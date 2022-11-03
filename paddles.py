from turtle import Turtle
LEFT_self_POSITION = (-350, 0)
RIGHT_self_POSITION = (350, 0)
UP = 90
DOWN = 270
DISTANCE = 20


class Paddles(Turtle):
    def __init__(self, position):
        """Takes a tuple as input and creates a Paddle at the given position"""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Moves Paddle up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves Paddle down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
