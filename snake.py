import turtle
import time
import random 

posp = 0.1

#Score

score=0
high_score=0

#Window configuration

window = turtle.Screen()

window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

#Snake Head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("DarkGreen")
head.penup() #Remove trail
head.goto(0,0) 
head.direction = "stop" 

#Snake body

body = []

#Food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup() #Without rastro
food.goto(0,100)

#Score text

text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()   
text.goto(0,260)
text.write("Score: 0    High Score: 0", align="center", font=("Courier", 24, "normal"))

#Functions

def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"   

def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Keyboard

window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

while True:
    window.update()

    #Border colision

    if head.xcor()>280 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #Hide the body
        for segment in body:
            segment.goto(1000,1000)

        body.clear()

        #Reset the score

        score=0
        text.clear()
        text.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    #Food colision
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("DarkOliveGreen")
        new_segment.penup()
        body.append(new_segment)

        #Increase score

        score+=1

        if score>high_score:
            high_score=score

        text.clear()
        text.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    #Move snake body

    totalSegments = len(body)

    for i in range(totalSegments - 1, 0, -1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x,y)

    if totalSegments > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)

    mov()

    #Body colision

    for segment in body:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #Hide the body
            for segment in body:
                segment.goto(1000,1000)
            body.clear()

            #Reset the score

            score=0
            text.clear()
            text.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(posp)
