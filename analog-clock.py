#Clock Assignment
import turtle
import datetime
screen=turtle.Screen()
Clock=turtle.Turtle()
#screen setup
screen.bgcolor("light green")
screen.title("Clock Assignment")
screen.setup(width=1000, height=700)
pen=turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(0,0)
#Draw Layout of Clock
def draw_layout_of_clock(clock,x,y,radius, angle,color): #In this function the first arg is a positional argument
    clock.speed(0)
    clock.penup()
    clock.color(color)
    clock.begin_fill() #call the turtle to fill circle before drawn
    clock.goto(x+radius,y) # Move turtle along x axis by distance of radius and 
    clock.setheading(angle) #set the turtle head to the given angle
    clock.pendown()
    clock.circle(radius)# draw circle
    clock.end_fill() #Fill circle after last call of draw_layout_of_clock to begin fill.
    clock.penup()
    clock.goto(0,0)

draw_layout_of_clock(Clock,0,0,300,90,"dimgray") #Outercircle to decorate  outerside of clock 
draw_layout_of_clock(Clock,0, 0,280,90 ,"darkgray")# 
draw_layout_of_clock(Clock,0,0,8,90,"black")#inner most circle
#Writing clock points on the circle by using hash 
Hash=turtle.Turtle() 
Hash.hideturtle()
pen.penup()
pen.goto(0,0)
Hash.setheading(90)
Hash.speed(0)
for i in range (60):
    if i%5==0:
        Hash.penup()
        Hash.pencolor("orange")
        Hash.pensize(4)
        Hash.forward(260)
        Hash.pendown()
        Hash.forward(19)
        Hash.penup()
        Hash.goto(0,0)
        Hash.right(6)
    else:
       Hash.pensize(2)
       Hash.pencolor("black")
       Hash.speed(0)
       Hash.goto(0,0)
       Hash.forward(274)
       Hash.pendown()
       Hash.forward(5)
       Hash.penup()
       Hash.goto(0,0)
       Hash.right(6) 

pen.color("black")
pen.penup()
Clock_Number=turtle.Turtle()
Clock_Number.setheading(60)
Clock_Number.speed(0)
i=1
#The following while loop writes the number of clock at the directed position 1-12
while i<=12:
    Clock_Number.penup()
    Clock_Number.goto(0,-15)
    Clock_Number.forward(240)
    Clock_Number.pendown()
    Clock_Number.write(i,align="center",font=("Stencil",20,"normal"))
    Clock_Number.penup()
    Clock_Number.goto(0,0)
    Clock_Number.right(30)
    i=i+1
#drawing hour hand shape,size and color
Hour_hand=turtle.Turtle()
Hour_hand.color ("black")
Hour_hand.shape("arrow")
Hour_hand.speed(10)
Hour_hand.shapesize(stretch_wid=0.3, stretch_len=15)
#Drawing minute hand shape,size and color
Minute_hand=turtle.Turtle()
Minute_hand.color("green")
Minute_hand.shape("arrow")
Minute_hand.speed(10)
Minute_hand.shapesize(stretch_wid=0.3, stretch_len=20)

#draw second hand shape,size and color
Second_Hand=turtle.Turtle()
Second_Hand.color("red")
Second_Hand.shape("arrow")
Second_Hand.speed(10)
Second_Hand.shapesize(stretch_wid=0.2, stretch_len=26)

#The following function is to  Move Hour hand clockwise by converting current hour and minute to angle in degree
#because the point where angle is (0) degree time is 3 O'clock 
#multiplied by -30 means to move hour hand clockwise and angle goes from 0 to -360 in 24 hours.

def Move_Hour_Hand():
    Current_hr=datetime.datetime.now().hour # get Current hour from computer
    Current_Min=datetime.datetime.now().minute 
    angle = (Current_hr - 3) * -30 +(-0.5*Current_Min) #move hour hand smoothly that is for every 2 minute move by -1 degree
    Hour_hand.setheading(angle)
screen.ontimer(Move_Hour_Hand, 60000)

#The following function is to move Minute hand by converting current minute and second to angle in degree
#Here at point where turtle angle is 0 degree minute is 15.The measure of angle between min and min is 6 degree 
#when second hand move by angle of -10 degree, minute hand move by -1 degree
def Move_Minute_Hand():
    Current_Min=datetime.datetime.now().minute
    Current_Sec=datetime.datetime.now().second
    angle= ((Current_Min - 15) *-6)+(-Current_Sec * 0.1) 
    Minute_hand.setheading(angle)
    screen.ontimer(Move_Minute_Hand,1000) # Here ontimer checks the function called move_minute_hand after 1 sec
#moving second hand
def Move_Second_Hand():
    Current_Sec=datetime.datetime.now().second
    angle= (Current_Sec - 15) * -6
    Second_Hand.setheading(angle)
    screen.ontimer(Move_Second_Hand,1) #Here ontimer checks the move_second_hand function after 1 milisecond to make second precise.
#The following ontimer is an infinite loop.
screen.ontimer(Move_Hour_Hand, 1)
screen.ontimer(Move_Minute_Hand, 1)
screen.ontimer(Move_Second_Hand, 1)
turtle.hideturtle()
screen.mainloop()

