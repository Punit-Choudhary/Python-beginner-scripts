from turtle import *

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_seg(position)

    def add_seg(self, position):
        seg_new = Turtle("square")
        seg_new.color("white")
        seg_new.penup()
        seg_new.goto(position)
        self.segments.append(seg_new)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_seg(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            pass

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            pass

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            pass

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            pass
