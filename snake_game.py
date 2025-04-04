from turtle import Screen, Turtle
import time
import random

segements = []

def up():
    if new_segment.heading() != 270:
        new_segment.setheading(90)
def down():
    if new_segment.heading() != 90:
        new_segment.setheading(270)
def left():
    if new_segment.heading() != 0:
        new_segment.setheading(180)
def right():
    if new_segment.heading() != 180:
        new_segment.setheading(0)

# Pantalla
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("purple")
screen.title("KimsssSnake game")
screen.tracer(0)

# Serpiente
new_segment = Turtle("square")
new_segment.color("black")
new_segment.penup()
new_segment.goto(0, 0)
segements.append(new_segment)

# Food
food = Turtle("circle")
food.color("beige")
food.penup()
random_x = random.randint(-280, 280)
random_y = random.randint(-280, 280)
food.goto(random_x, random_y)

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

while True:
    screen.update()
    time.sleep(0.2)

    # deted touch food
    if new_segment.distance(food) < 15:
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        food.goto(random_x, random_y)

        next_segment = Turtle("square")
        next_segment.color("black")
        next_segment.penup()
        segements.append(next_segment)

    if len(segements) > 1:
        for i in range(len(segements) - 1, 0, -1):
            segements[i].goto(segements[i - 1].xcor(), segements[i - 1].ycor())

    new_segment.forward(20)




screen.exitonclick()
