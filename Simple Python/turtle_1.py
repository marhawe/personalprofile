'''
Project 1 - Turtle Art - Spring 2020
Author: Marhawe Asmerom @howie18

This program uses turtle graphics to generate a drawing of Lane Stadium

I have neither given or received unauthorized assistance on this assignment.
Signed: Marhawe Asmerom
'''



import turtle

turtle.setup(600, 600, None, None)
turtle.title('Project 1 - Turtle Art')

turtle.speed(10) #adjust the speed of the terminal
turtle.bgcolor("forest green") # making background color
turtle.pensize(10)

turtle.penup() # creating thick black frame
turtle.goto(-637, 342)
turtle.pendown()
turtle.pencolor('black')
turtle.forward(1263)
turtle.pencolor('black')
turtle.right(90)
turtle.forward(670)
turtle.pencolor('black')
turtle.right(90)
turtle.forward(1263)
turtle.pencolor('black')
turtle.right(90)
turtle.forward(670)

turtle.pensize(4) # making the white end zone boundry 
turtle.penup()
turtle.goto(-630, 336)
turtle.pendown()
turtle.pencolor('white')
turtle.right(90)
turtle.forward(225)
turtle.pencolor('white')
turtle.right(90)
turtle.forward(660)
turtle.pencolor('white')
turtle.right(90)
turtle.forward(225)
turtle.pencolor('white')
turtle.right(90)
turtle.forward(660)


turtle.penup() # making the white end zone boundry 
turtle.goto(620, 336)
turtle.pendown()
turtle.pencolor('white')
turtle.left(90)
turtle.forward(225)
turtle.pencolor('white')
turtle.left(90)
turtle.forward(660)
turtle.pencolor('white')
turtle.left(90)
turtle.forward(225)
turtle.pencolor('white')
turtle.left(90)
turtle.forward(660)

turtle.pensize(2)
turtle.pencolor('white')
turtle.penup()
turtle.goto(395, 275)
turtle.pendown()
turtle.left(90)
turtle.forward(800)


turtle.penup() 
turtle.goto(395, -275)
turtle.pendown()
turtle.right(90)
turtle.left(90)
turtle.forward(800)

turtle.right(180)

turtle.pensize(1.25) 

for i in range(10): # loop to create hashmarks on field
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(50)
    turtle.backward(1100)
    turtle.forward(1100)
    turtle.left(90)

turtle.penup()
turtle.goto(395, 275)
turtle.pendown()

turtle.right(180)
for i in range(10):
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(10)
    turtle.backward(20)
    turtle.forward(10)
    turtle.left(90)

turtle.penup()
turtle.goto(-175, 50) # creation on the VT midfield logo
turtle.pendown()
turtle.pensize(8)
turtle.pencolor('#cc5500')
turtle.fillcolor('#630031')
turtle.begin_fill()
turtle.forward(50)
turtle.setheading(315)
turtle.forward(200)
turtle.setheading(45)
turtle.forward(200)
turtle.setheading(180)
turtle.forward(75)
turtle.setheading(225)
turtle.forward(100)
turtle.setheading(135)
turtle.forward(100)
turtle.setheading(180)
turtle.forward(45)
turtle.end_fill()
turtle.penup()
turtle.goto(60, 50)
turtle.pendown()

turtle.pensize(8) # creating T in VT midfield logo
turtle.pencolor('#cc5500')
turtle.fillcolor('#630031')
turtle.begin_fill()
turtle.forward(50)
turtle.setheading(0)
turtle.forward(175)
turtle.setheading(270)
turtle.forward(50)
turtle.setheading(180)
turtle.forward(50)
turtle.setheading(270)
turtle.forward(100)
turtle.setheading(180)
turtle.forward(50)
turtle.setheading(90)
turtle.forward(100)
turtle.setheading(180)
turtle.forward(80)
turtle.setheading(50)
turtle.forward(60)
turtle.end_fill()

turtle.penup() # G block letter with maroon pen and orange fill
turtle.goto(-580, -100)
turtle.pendown()
turtle.pencolor('#630031')
turtle.fillcolor('#cc5500')

turtle.begin_fill()
turtle.setheading(0)
turtle.forward(75)
turtle.setheading(45)
turtle.forward(50)
turtle.setheading(90)
turtle.forward(75)
turtle.setheading(180)
turtle.forward(50)
turtle.setheading(90)
turtle.forward(18)
turtle.setheading(180)
turtle.forward(20)
turtle.setheading(270)
turtle.forward(65)
turtle.setheading(0)
turtle.forward(20)
turtle.setheading(90)
turtle.forward(15)
turtle.setheading(0)
turtle.forward(21)

turtle.penup()
turtle.goto(-580, -100)
turtle.pendown()
turtle.setheading(135)
turtle.forward(50)
turtle.setheading(90)
turtle.forward(60)
turtle.setheading(0)
turtle.forward(30)
turtle.setheading(270)
turtle.forward(60)
turtle.setheading(0)
turtle.forward(65)
turtle.setheading(45)
turtle.forward(30)
turtle.setheading(90)
turtle.forward(20)
turtle.end_fill()

turtle.penup()
turtle.goto(-475, 110) # making the O letter (using the octagon shape)
turtle.pendown()
turtle.pencolor('#630031')
turtle.fillcolor('#cc5500')

turtle.pensize(8)
turtle.begin_fill()
turtle.forward(50)
turtle.setheading(135)
turtle.forward(50)
turtle.setheading(180)
turtle.forward(50)
turtle.setheading(225)
turtle.forward(50)
turtle.setheading(270)
turtle.forward(50)
turtle.setheading(315)
turtle.forward(50)
turtle.setheading(0)
turtle.forward(50)
turtle.setheading(45)
turtle.forward(50)
turtle.setheading(45)

    
turtle.end_fill()


turtle.penup()
turtle.goto(-510, 125)
turtle.pendown()
turtle.fillcolor('#228b22')
turtle.begin_fill()
turtle.setheading(90)
turtle.forward(25)
turtle.setheading(135)
turtle.forward(25)
turtle.setheading(180)
turtle.forward(25)
turtle.setheading(225)
turtle.forward(25)
turtle.setheading(270)
turtle.forward(25)
turtle.setheading(315)
turtle.forward(25)
turtle.setheading(0)
turtle.forward(25)
turtle.setheading(45)
turtle.forward(25)
turtle.setheading(45)
turtle.end_fill()

turtle.pensize(6)

turtle.fillcolor('#cc5500')
turtle.begin_fill()
turtle.penup() # Making the letter H in the south endzone
turtle.goto(425,-300)
turtle.pendown()
turtle.setheading(90)
turtle.forward(50)
turtle.setheading(0)
turtle.forward(150)
turtle.setheading(270)
turtle.forward(50)
turtle.setheading(180)
turtle.forward(150)
turtle.end_fill()
turtle.penup() 
turtle.goto(425,-200)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(90)
turtle.forward(50)
turtle.setheading(0)
turtle.forward(150)
turtle.setheading(270)
turtle.forward(50)
turtle.setheading(180)
turtle.forward(150)
turtle.end_fill()
turtle.penup() # 
turtle.goto(480,-250) 
turtle.pendown()
turtle.begin_fill()
turtle.setheading(90)
turtle.forward(50)
turtle.setheading(0)
turtle.forward(30)
turtle.setheading(270)
turtle.forward(50)
turtle.end_fill()

turtle.penup()
turtle.goto(580,-100) 
turtle.pendown()


turtle.pencolor('#630031') # Hokie Colors as fill and pen color
turtle.fillcolor('#cc5500')


turtle.begin_fill() # Making O in the endzone
turtle.setheading(90)
turtle.forward(60)
turtle.setheading(135)
turtle.forward(60)
turtle.setheading(180)
turtle.forward(60)
turtle.setheading(225)
turtle.forward(60)
turtle.setheading(270)
turtle.forward(60)
turtle.setheading(315)
turtle.forward(60)
turtle.setheading(0)
turtle.forward(60)
turtle.setheading(45)
turtle.forward(60)
turtle.setheading(45)

    
turtle.end_fill()


turtle.penup() #inner O with a green fill
turtle.goto(540, -84)
turtle.pendown()
turtle.fillcolor('#228b22')
turtle.begin_fill()
turtle.setheading(90)
turtle.forward(30)
turtle.setheading(135)
turtle.forward(30)
turtle.setheading(180)
turtle.forward(30)
turtle.setheading(225)
turtle.forward(30)
turtle.setheading(270)
turtle.forward(30)
turtle.setheading(315)
turtle.forward(30)
turtle.setheading(0)
turtle.forward(30)
turtle.setheading(45)
turtle.forward(30)
turtle.setheading(45)
turtle.end_fill()

turtle.fillcolor('#cc5500')

turtle.penup() # Letter K in block letters
turtle.goto(425, 35)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.forward(150)
turtle.setheading(90)
turtle.forward(40)
turtle.setheading(180)
turtle.forward(150)
turtle.setheading(270)
turtle.forward(40)
turtle.end_fill()

turtle.penup()
turtle.goto(530,35)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(135)
turtle.forward(150)
turtle.setheading(270)
turtle.forward(40)
turtle.setheading(315)
turtle.forward(50)
turtle.end_fill()


turtle.penup() 
turtle.goto(490, 35)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(45)
turtle.forward(130)
turtle.setheading(180)
turtle.forward(40)
turtle.setheading(225)
turtle.forward(95)
turtle.end_fill()




turtle.penup() # the letter I in the endzone
turtle.goto(425,150)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.forward(150)
turtle.setheading(90)
turtle.forward(40)
turtle.setheading(180)
turtle.forward(150)
turtle.setheading(270)
turtle.forward(40)
turtle.end_fill()

turtle.penup() # the letter E in the endzone
turtle.goto(425,200)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.forward(150)
turtle.setheading(90)
turtle.forward(40)
turtle.setheading(180)
turtle.forward(150)
turtle.setheading(270)
turtle.forward(40)
turtle.end_fill()
turtle.penup() # the letter E in the endzone
turtle.goto(425,200)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(90)
turtle.forward(100)
turtle.setheading(0)
turtle.forward(40)
turtle.setheading(270)
turtle.forward(100)
turtle.end_fill()
turtle.penup() # the letter E in the endzone
turtle.goto(480,200)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(90)
turtle.forward(75)
turtle.setheading(0)
turtle.forward(40)
turtle.setheading(270)
turtle.forward(75)
turtle.end_fill()
turtle.penup() # the letter E in the endzone
turtle.goto(535,200)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(90)
turtle.forward(100)
turtle.setheading(0)
turtle.forward(40)
turtle.setheading(270)
turtle.forward(100)
turtle.end_fill()



turtle.penup() # Prompts the "Welcome to Lane Stadium" text
turtle.goto(5, 287)
turtle.pendown()
turtle.color('Black')
style = ('Comic Sans', 40, 'bold italic')
turtle.write('Welcome to Lane Stadium!', font=style, align='center')
turtle.hideturtle()
