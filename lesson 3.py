import turtle

x=26
z=26
y=0


shelly=turtle.Turtle()
shelly.pensize(5)
colors=[]
colors=['red','orange','yellow','green','blue','indigo', 'violet']
while x<367:
    shelly.penup()
    shelly.goto(-x,-x)
    shelly.color(colors[y])
    shelly.pendown()
    shelly.goto(x,-x)
    shelly.goto(x,x)
    shelly.goto(-x,x)
    shelly.goto(-x,-x)
    y=y+1
    if y>6:
        y=0
    x=x+26


while z<367:
    shelly.penup()
    shelly.goto(z,0)
    shelly.pendown()
    shelly.color(colors[y])
    shelly.goto(0,z)
    shelly.goto(-z,0)
    shelly.goto(0,-z)
    shelly.goto(z,0)
    y=y+1
    if y>6:
        y=0
    z=z+26
