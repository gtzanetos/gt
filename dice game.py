import turtle
import random
shelly=turtle.Turtle()
dice=[0,0,0,0,0,0]
i=0
you=0
them=0
x1=[-400,350,-400,350,-400,350]
x2=[-250,200,-250,200,-250,200]
y1=[175,175,-25,-25,-225,-225]
y2=[25,25,-175,-175,-375,-375]

xnumber=[-325,275,-325,275,-325,275]
ynumber=[100,100,-100,-100,-300,-300]


while(i<6):
    dice[i]=random.randint(1,6)
    i=i+1

print(dice[0])
print(dice[1])
print(dice[2])
print(dice[3])
print(dice[4])
print(dice[5])
you=int(dice[0])+int(dice[2])+int(dice[4])
them=int(dice[1])+int(dice[3])+int(dice[5])
yousc=str(you)
themsc=str(them)
print("you"+yousc)
print("them"+themsc)

turtle.penup()
turtle.goto(-400,375)
i=0
turtle.write("Welcome to the game! You and an opponent will each roll the dice 3 times", font= ("Arial", 15, "normal"))
turtle.goto(-300,345)
turtle.write("Whoever gets a higher total score wins!", font= ("Arial", 15, "normal"))
turtle.goto(-360,250)
turtle.write("Your Dice", font= ("Arial", 15, "normal"))
turtle.goto(200,250)
turtle.write("Your Opponent's Dice", font= ("Arial", 15, "normal"))

while(i<6):
    turtle.goto(x1[i],y1[i])
    turtle.pendown()
    turtle.goto(x2[i],y1[i])
    turtle.goto(x2[i],y2[i])
    turtle.goto(x1[i],y2[i])
    turtle.goto(x1[i],y1[i])
    turtle.penup()
    turtle.goto(xnumber[i],ynumber[i])
    turtle.pendown()
    turtle.write(dice[i], font= ("Arial", 15, "normal"))
    turtle.penup()
       
    i=i+1

turtle.goto(-50,50)
turtle.write("Your total is "+yousc, font= ("Arial", 15, "normal"))
turtle.goto(-100,0)
turtle.write("Your opponent's total is "+themsc, font= ("Arial", 15, "normal"))
turtle.goto(-50,-50)

if(yousc>themsc):
    turtle.write("You win!! :)", font= ("Arial", 15, "normal"))

if(yousc<themsc):
    turtle.write("You lose :(", font= ("Arial", 15, "normal"))

if(yousc==themsc):
    turtle.write("It is a tie", font= ("Arial", 15, "normal"))
    
