'''
Project 2 - Scores Analysis and Bar Chart - Spring 2020
Author: <Marhawe Asmerom @howie18>

This program dissects the process of using a while loop and for loop to parse through a input file by
being able find count , average , max , and min. Using a function with certain parameters to make a bar graph
from the data compiled from the input text file. The function 

I have neither given or received unauthorized assistance on this assignment.
Signed: Marhawe Asmerom
'''
import turtle # importing the turtle module

sum = 0 # sets variables to zero
max = 0
min = 110
process = 'y'
count = 0


def draw_bar (x, y, color, height , text) : #main function that draws rectangles with text , location , height , color
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.setheading(90)
    turtle.forward(height)       
    turtle.right(90)
    turtle.forward(50)            
    turtle.right(90)
    turtle.forward(height)        
    turtle.left(90)
    turtle.end_fill()
    turtle.goto(x,y)
    turtle.write(text)

while process == 'y' or process =='yes' : # while the loop that checks for numerous file inputs , if (yes / y ) runs through the while and for loop
        
    filename = input('Please Enter File Name : ') # input the filename
    file = open(filename) 
    lines = file.readline()
    print('Result for ' + lines, end='')
    number_of_90s = 0
    number_of_80s = 0
    number_of_70s = 0
    number_of_60s = 0
    number_of_less_than_60 = 0
    for line in file: # inner loop that finds min , max , count , average
        num = int(line)
        count += 1
        num = int(line.split(",")[0]) # strips the line for the number
        if (num > 89): # begins a count for the graph 
            number_of_90s +=1
        elif (num > 80):
            number_of_80s +=1
        elif (num > 70):
            number_of_70s +=1
        elif (num > 60):
            number_of_60s +=1
        else :
            number_of_less_than_60 += 1
        if (max < num): # finds max
            max = num
        if (min > num): # finds min
            min = num
        sum = sum + num  
        average = sum / count; # uses sum and count to find average
        
    print('Count is', count )
    print('Maximum number is', max) 
    print('Minimum number is', min)
    print('The average is', round(average, 2))
    draw_bar(0, 0, 'green', number_of_90s / count * 100 * 5, "90s") # draws bar based on location , fill color , length , and a text
    draw_bar(50, 0, 'blue', number_of_80s / count * 100 * 5, "80s")
    draw_bar(100, 0, 'red', number_of_70s / count * 100 * 5, "70s")
    draw_bar(150, 0, 'orange', number_of_60s / count * 100 * 5 , "60s")
    draw_bar(200, 0, 'pink', number_of_less_than_60 / count * 100 * 5 , "Less than 60s" )
    
    count = 0 #resets sum and count to zero for a second file 
    sum = 0
    
    turtle.reset() # results reset if there is another input file
    turtle.hideturtle()

    process = input('Shall I process another file (Y/N): ') # asks if there is another text file to input 
    process = process.lower() 
    if process == 'n' or process =='no' : # if the answer is (no / n) proceeds to print the statement
        print("Have a nice day") 
    
   
    





    




