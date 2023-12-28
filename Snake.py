# Snake Game
import turtle
import time
import random

delay = 0.1

win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

# Border
border = turtle.Turtle()
border.speed(0)
border.color("blue")
border.penup()
border.goto(-295, 295)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(580)
    border.rt(90)
border.hideturtle()

# Score
score = 0
high_score = 0

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 255)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# Keyboard bindings
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_up, "Up")

win.onkeypress(go_down, "s")
win.onkeypress(go_down, "Down")

win.onkeypress(go_right, "d")
win.onkeypress(go_right, "Right")

win.onkeypress(go_left, "a")
win.onkeypress(go_left, "Left")


# Main Game Loop
while True:
    win.update()

    # Check for border collisions
    if head.ycor() > 290:
        head.goto(head.xcor(), -280)
        head.direction = 'up'

    if head.ycor() < -290:
        head.goto(head.xcor(), 280)
        head.direction = 'down'

    if head.xcor() > 290:
        head.goto(-280, head.ycor())
        head.direction = 'right'

    if head.xcor() < -290:
        head.goto(280, head.ycor())
        head.direction = 'left'

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001
        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = "stop"

            # Reset delay
            delay = 0.1

            # Reset the score
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            # Hide segments
            for segment in segments:
                segment.hideturtle()
            # Clear the segments list
            segments.clear()

    time.sleep(delay)
