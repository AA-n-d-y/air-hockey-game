# Program for an Air Hockey Game using the Turtle Library
#
#
#################################################


### Imports and creating the window

import turtle
window = turtle.Screen()
window.setup(height = 600, width = 1200)
window.bgcolor("#3E8EDE")
window.title("Air Hockey")
window.tracer(0)


### Instructions for starting the game

starter = turtle.Turtle()
starter.speed(0)
starter.hideturtle()
starter.penup()
starter.goto (0, 0)
starter.write("Press your spacebar key to start the game", font = ("Roboto", 25), align = "center")
starter.goto (0, -50)
starter.write("First to 3 goals wins", font = ("Roboto", 25), align = "center")
starter.goto (0, -100)
starter.write("Click to exit the program", font = ("Roboto", 25), align = "center")


### Mallet instructions

instructions = turtle.Turtle()
instructions.speed(0)
instructions.hideturtle()
instructions.penup()
instructions.goto(-10, -250)
instructions.write("Left mallet: W A S D keys to move            Right mallet: Arrow keys to move", \
        font = ("Roboto", 15), align = "center")


### Scoreboard

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(0, 225)
scoreboard.write("0                                          0", font = ("Roboto", 35), \
        align = "center")
left_score = 0
right_score = 0


### Creating the arena

middleLine = turtle.Turtle()
middleLine.speed(0)
middleLine.shape("square")
middleLine.penup()
middleLine.goto(0, 0)
middleLine.color("white")
middleLine.shapesize(30, 0.5)

middleCircle = turtle.Turtle()
middleCircle.speed(0)
middleCircle.shape("circle")
middleCircle.penup()
middleCircle.goto(0, 0)
middleCircle.color("white")
middleCircle.shapesize(5.5)

leftGoal = turtle.Turtle()
leftGoal.speed(0)
leftGoal.shape("square")
leftGoal.penup()
leftGoal.goto(-590, 0)
leftGoal.color("white")
leftGoal.shapesize(10, 1)

rightGoal = turtle.Turtle()
rightGoal.speed(0)
rightGoal.shape("square")
rightGoal.penup()
rightGoal.goto(590, 0)
rightGoal.color("white")
rightGoal.shapesize(10, 1)


## Creating the mallets and the puck

leftMallet = turtle.Turtle()
leftMallet.speed(0)
leftMallet.shape("circle")
leftMallet.penup()
leftMallet.goto(-300, 0)
leftMallet.color("#ED2939")
leftMallet.shapesize(7)

rightMallet = turtle.Turtle()
rightMallet.speed(0)
rightMallet.shape("circle")
rightMallet.penup()
rightMallet.goto(300, 0)
rightMallet.color("#ED2939")
rightMallet.shapesize(7)

puck = turtle.Turtle()
puck.speed(0)
puck.shape("circle")
puck.penup()
puck.goto(0, 0)
puck.color("black")
puck.shapesize(3.5)
puck_y_speed = 150
puck_x_speed = 150


### Functions

## Left mallet controls

def leftMalletUp():
    leftMY = leftMallet.ycor()
    leftMY += 20
    leftMallet.sety(leftMY)
    if leftMY > 230:
        leftMY -= 20
        leftMallet.sety(leftMY)

def leftMalletDown():
    leftMY = leftMallet.ycor()
    leftMY -= 20
    leftMallet.sety(leftMY)
    if leftMY < -230:
        leftMY += 20
        leftMallet.sety(leftMY)

def leftMalletRight():
    leftMX = leftMallet.xcor()
    leftMX += 20
    leftMallet.setx(leftMX)
    if leftMX > 530:
        leftMX -= 20
        leftMallet.setx(leftMX)

def leftMalletLeft():
    leftMX = leftMallet.xcor()
    leftMX -= 20
    leftMallet.setx(leftMX)
    if leftMX < -530:
        leftMX += 20
        leftMallet.setx(leftMX)

## Right mallet controls

def rightMalletUp():
    rightMY = rightMallet.ycor()
    rightMY += 20
    rightMallet.sety(rightMY)
    if rightMY > 230:
        rightMY -= 20
        rightMallet.sety(rightMY)

def rightMalletDown():
    rightMY = rightMallet.ycor()
    rightMY -= 20
    rightMallet.sety(rightMY)
    if rightMY < -230:
        rightMY += 20
        rightMallet.sety(rightMY)

def rightMalletRight():
    rightMX = rightMallet.xcor()
    rightMX += 20
    rightMallet.setx(rightMX)
    if rightMX > 530:
        rightMX -= 20
        rightMallet.setx(rightMX)

def rightMalletLeft():
    rightMX = rightMallet.xcor()
    rightMX -= 20
    rightMallet.setx(rightMX)
    if rightMX < -530:
        rightMX += 20
        rightMallet.setx(rightMX)

## Function to start the game

def startG():
    global left_score
    global right_score
    global puck_x_speed
    global puck_y_speed
    starter.clear()

    while left_score < 3 and right_score < 3:
        window.update()

        ## Left mallet

            # Hitting the puck from the right
        if (leftMallet.xcor() + 70) >= (puck.xcor() - 35) and (leftMallet.xcor() + 70) <= \
        (puck.xcor() + 35) and (leftMallet.ycor() <= puck.ycor() + 20) and (leftMallet.ycor() \
        >= puck.ycor() - 20):
            puck.setx(puck.xcor() + puck_x_speed)

            # Hitting the puck from the left
        if (leftMallet.xcor() - 70) <= (puck.xcor() + 35) and (leftMallet.xcor() - 70) >= \
        (puck.xcor() - 35) and (leftMallet.ycor() <= puck.ycor() + 20) and (leftMallet.ycor() >= \
        puck.ycor() - 20):
            puck.setx(puck.xcor() - puck_x_speed)

            # Hitting the puck from the top        
        if (leftMallet.ycor() - 70) <= (puck.ycor() + 35) and (leftMallet.ycor() + 70) >= \
        (puck.ycor() - 35) and (leftMallet.xcor() <= puck.xcor() + 20) and (leftMallet.xcor() >= \
        puck.xcor() - 20):
            puck.sety(puck.ycor() - puck_y_speed)

            # Hitting the puck from the bottom
        if (leftMallet.ycor() + 70) >= (puck.ycor() - 50) and (leftMallet.ycor() - 70) <= \
        (puck.ycor() + 35) and (leftMallet.xcor() <= puck.xcor() + 20) and (leftMallet.xcor() >= \
        puck.xcor() - 20):
            puck.sety(puck.ycor() + puck_y_speed)

            # Hitting the puck from the top left
        if (leftMallet.xcor() + 35) >= (puck.xcor() - 35) and (leftMallet.xcor() + 35) <= \
        (puck.xcor() - 25) and (leftMallet.xcor() - 35) <= (puck.xcor() + 35) and \
        (leftMallet.ycor() >= puck.ycor()) and (leftMallet.ycor() - 70 <= puck.ycor()):
            puck.setx(puck.xcor() + puck_x_speed)
            puck.sety(puck.ycor() - puck_y_speed)

            # Hitting the puck from the top right
        if (leftMallet.xcor() - 35) <= (puck.xcor() + 35) and (leftMallet.xcor() - 35) >= \
        (puck.xcor() + 25) and (leftMallet.xcor() + 35) >= (puck.xcor() - 35) and \
        (leftMallet.ycor() >= puck.ycor()) and (leftMallet.ycor() - 70 <= puck.ycor()):
            puck.setx(puck.xcor() - puck_x_speed)
            puck.sety(puck.ycor() - puck_y_speed)

            # Hitting the puck from the bottom left
        if (leftMallet.xcor() + 35) >= (puck.xcor() - 35) and (leftMallet.xcor() + 35) <= \
        (puck.xcor() - 25) and (leftMallet.xcor() - 35) <= (puck.xcor() + 35) and \
        (leftMallet.ycor() <= puck.ycor()) and (leftMallet.ycor() + 70 >= puck.ycor()):
            puck.setx(puck.xcor() + puck_x_speed)
            puck.sety(puck.ycor() + puck_y_speed)

            # Hitting the puck from the bottom right
        if (leftMallet.xcor() - 35) <= (puck.xcor() + 35) and (leftMallet.xcor() - 35) >= \
        (puck.xcor() + 25) and (leftMallet.xcor() + 35) >= (puck.xcor() - 35) and \
        (leftMallet.ycor() <= puck.ycor()) and (leftMallet.ycor() + 70 >= puck.ycor()):
            puck.setx(puck.xcor() - puck_x_speed)
            puck.sety(puck.ycor() + puck_y_speed)


        ## Right mallet

            # Hitting the puck from the left
        if (rightMallet.xcor() + 70) >= (puck.xcor() - 35) and (rightMallet.xcor() + 70) <= \
        (puck.xcor() + 35) and (rightMallet.ycor() <= puck.ycor() + 20) and (rightMallet.ycor() \
        >= puck.ycor() - 20):
            puck.setx(puck.xcor() + puck_x_speed)

            # Hitting the puck from the right
        if (rightMallet.xcor() - 70) <= (puck.xcor() + 35) and (rightMallet.xcor() - 70) >= \
        (puck.xcor() - 35) and (rightMallet.ycor() <= puck.ycor() + 20) and \
        (rightMallet.ycor() >= puck.ycor() - 20):
            puck.setx(puck.xcor() - puck_x_speed)

            # Hitting the puck from the top
        if (rightMallet.ycor() - 70) <= (puck.ycor() + 35) and (rightMallet.ycor() + 70) >= \
        (puck.ycor() - 35) and (rightMallet.xcor() <= puck.xcor() + 20) and (rightMallet.xcor() \
        >= puck.xcor() - 20):
            puck.sety(puck.ycor() - puck_y_speed)

            # Hitting the puck from the bottom
        if (rightMallet.ycor() + 70) >= (puck.ycor() - 50) and (rightMallet.ycor() - 70) <= \
        (puck.ycor() + 35) and (rightMallet.xcor() <= puck.xcor() + 20) and (rightMallet.xcor() \
        >= puck.xcor() - 20):
            puck.sety(puck.ycor() + puck_y_speed)

            # Hitting the puck from the top left
        if (rightMallet.xcor() + 35) >= (puck.xcor() - 35) and (rightMallet.xcor() + 35) <= \
        (puck.xcor() - 25) and (rightMallet.xcor() - 35) <= (puck.xcor() + 35) and \
        (rightMallet.ycor() >= puck.ycor()) and (rightMallet.ycor() - 70 <= puck.ycor()):
            puck.setx(puck.xcor() + puck_x_speed)
            puck.sety(puck.ycor() - puck_y_speed)

            # Hitting the puck from the top right
        if (rightMallet.xcor() - 35) <= (puck.xcor() + 35) and (rightMallet.xcor() - 35) >= \
        (puck.xcor() + 25) and (rightMallet.xcor() + 35) >= (puck.xcor() - 35) and \
        (rightMallet.ycor() >= puck.ycor()) and (rightMallet.ycor() - 70 <= puck.ycor()):
            puck.setx(puck.xcor() - puck_x_speed)
            puck.sety(puck.ycor() - puck_y_speed)

            # Hitting the puck from the bottom left
        if (rightMallet.xcor() + 35) >= (puck.xcor() - 35) and (rightMallet.xcor() + 35) \
        <= (puck.xcor() - 25) and (rightMallet.xcor() - 35) <= (puck.xcor() + 35) and \
        (rightMallet.ycor() <= puck.ycor()) and (rightMallet.ycor() + 70 >= puck.ycor()):
            puck.setx(puck.xcor() + puck_x_speed)
            puck.sety(puck.ycor() + puck_y_speed)

            # Hitting the puck from the bottom right
        if (rightMallet.xcor() - 35) <= (puck.xcor() + 35) and (rightMallet.xcor() - 35) >= \
        (puck.xcor() + 25) and (rightMallet.xcor() + 35) >= (puck.xcor() - 35) and \
        (rightMallet.ycor() <= puck.ycor()) and (rightMallet.ycor() + 70 >= puck.ycor()):
            puck.setx(puck.xcor() - puck_x_speed)
            puck.sety(puck.ycor() + puck_y_speed)


        ## Puck boundaries

            # Puck hitting the top
        if puck.ycor() > 290:
            puck.sety(puck.ycor() - 120)
        
            # Puck hitting the bottom
        if puck.ycor() < -290:
            puck.sety(puck.ycor() + 120)

            # Puck hitting the right
        if puck.xcor() > 590:
            puck.setx(puck.xcor() - 120)

            # Puck hitting the left
        if puck.xcor() < -590:
            puck.setx(puck.xcor() + 120)


        ## Mallet hitting mallet

            # Left mallet hitting right mallet from the left
        if leftMallet.xcor() + 70 > rightMallet.xcor() - 70 and leftMallet.xcor() + 70 < \
        rightMallet.xcor() and leftMallet.ycor() <= rightMallet.ycor() + 70 and leftMallet.ycor() \
        >= rightMallet.ycor() - 70:
            leftMallet.setx(leftMallet.xcor() - 70)
            rightMallet.setx(rightMallet.xcor() + 10)
        
            # Left mallet hitting right mallet from the right
        if leftMallet.xcor() - 70 < rightMallet.xcor() + 70 and leftMallet.xcor() - 70 > \
        rightMallet.xcor() and leftMallet.ycor() <= rightMallet.ycor() + 70 and leftMallet.ycor() \
        >= rightMallet.ycor() - 70:
            leftMallet.setx(leftMallet.xcor() + 70)
            rightMallet.setx(rightMallet.xcor() - 10)

            # Left mallet hitting right mallet from the top
        if leftMallet.xcor() + 30 >= rightMallet.xcor() - 30 and leftMallet.xcor() - 30 <= \
        rightMallet.xcor() + 30 and leftMallet.ycor() - 70 < rightMallet.ycor() + 70 and \
        leftMallet.ycor() - 70 > rightMallet.ycor():
            leftMallet.sety(leftMallet.ycor() + 70)
            rightMallet.sety(rightMallet.ycor() - 10)
        
            # Left mallet hitting right mallet from the bottom
        if leftMallet.xcor() + 30 >= rightMallet.xcor() - 30 and leftMallet.xcor() - 30 <= \
        rightMallet.xcor() + 30 and leftMallet.ycor() + 70 > rightMallet.ycor() - 70 and \
        leftMallet.ycor() + 70 < rightMallet.ycor():
            leftMallet.sety(leftMallet.ycor() - 70)
            rightMallet.sety(rightMallet.ycor() + 10)

            # Right mallet hitting left mallet from the left
        if rightMallet.xcor() + 70 > leftMallet.xcor() - 70 and rightMallet.xcor() + 70 < \
        leftMallet.xcor() and rightMallet.ycor() <= leftMallet.ycor() + 70 and rightMallet.ycor() \
        >= leftMallet.ycor() - 70:
            rightMallet.setx(rightMallet.xcor() - 70)
            leftMallet.setx(leftMallet.xcor() + 10 )
        
            # Right mallet hitting right mallet from the right
        if rightMallet.xcor() - 70 < leftMallet.xcor() + 70 and rightMallet.xcor() - 70 > \
        leftMallet.xcor() and rightMallet.ycor() <= leftMallet.ycor() + 70 and rightMallet.ycor() \
        >= leftMallet.ycor() - 70:
            rightMallet.setx(rightMallet.xcor() + 70)
            leftMallet.setx(leftMallet.xcor() - 10 )

            # Right mallet hitting left mallet from the top
        if rightMallet.xcor() + 30 >= leftMallet.xcor() - 30 and rightMallet.xcor() - 30 <= \
        leftMallet.xcor() + 30 and rightMallet.ycor() - 70 < leftMallet.ycor() + 70 and \
        rightMallet.ycor() - 70 > leftMallet.ycor():
            rightMallet.sety(rightMallet.ycor() + 70)
            leftMallet.sety(leftMallet.ycor() - 10 )
        
            # Right mallet hitting left mallet from the bottom
        if rightMallet.xcor() + 30 >= leftMallet.xcor() - 30 and rightMallet.xcor() - 30 <= \
        leftMallet.xcor() + 30 and rightMallet.ycor() + 70 > leftMallet.ycor() - 70 and \
        rightMallet.ycor() + 70 < leftMallet.ycor():
            rightMallet.sety(rightMallet.ycor() - 70)
            leftMallet.sety(leftMallet.ycor() + 10 )


        ## Scoring

        if puck.xcor() > 599 and puck.ycor() <= 65 and puck.ycor() >= -65:
            scoreboard.clear()
            instructions.clear()
            left_score += 1
            scoreboard.write(f"{left_score}                                          {right_score}", \
                    font = ("Roboto", 35), align = "center")
            puck.goto(0,0)

        if puck.xcor() < -599 and puck.ycor() <= 65 and puck.ycor() >= -65:
            scoreboard.clear()
            instructions.clear()
            right_score += 1
            scoreboard.write(f"{left_score}                                          {right_score}", \
                    font = ("Roboto", 35), align = "center")
            puck.goto(0,0)


    ## End Screen

    endScreen = turtle.Turtle()
    endScreen.speed(0)
    endScreen.hideturtle()
    endScreen.penup()
    endScreen.goto(0, 0)

    if left_score > right_score:
        endScreen.write("Left Player Wins", font = ("Roboto", 35), align = "center")

    elif right_score > left_score:
        endScreen.write("Right Player Wins", font = ("Roboto", 35), align = "center")


### Keystrokes

window.onkeypress(leftMalletUp, "w")
window.onkeypress(leftMalletDown, "s")
window.onkeypress(leftMalletRight, "d")
window.onkeypress(leftMalletLeft, "a")
window.onkeypress(rightMalletUp, "Up")
window.onkeypress(rightMalletDown, "Down")
window.onkeypress(rightMalletRight, "Right")
window.onkeypress(rightMalletLeft, "Left")
window.onkeypress(startG, "space")
window.listen()

# Exiting the game
window.exitonclick()



### End of program
