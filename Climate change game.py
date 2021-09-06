from tkinter import*
import random
import time

window=Tk()
window.title('Climate Change')


canvas=Canvas(window, width=1200,height=800)
canvas.pack()

label=canvas.create_text(400,200,text='')
label=canvas.create_text(400,220,text='')
label=canvas.create_text(400,240,text='')

coalnum=20
oilnum=15
steelnum=5
concretenum=10

news=Label(window,text="Welcome to the Game")
news.pack()
coins=0
coins_display=Label(window, text="Coins :" +str(coins))
coins_display.pack()

weapons=0
weapons_display=Label(window, text="weapons :" +str(weapons))
weapons_display.pack()

food=1000
food_display=Label(window, text="food :" +str(food))
food_display.pack()

trees=0

carbon=0
carbon_display=Label(window, text="Carbon Emitted :" +str(carbon))
carbon_display.pack()


circle=canvas.create_oval(35,370,65,400, fill='red')
img=PhotoImage(file="gold bars no background.png")
store=PhotoImage(file="food store.png")
weap=PhotoImage(file="weapons store.png")
nursery=PhotoImage(file="tree store.png")
tree=PhotoImage(file="tree.png")
oil=PhotoImage(file="oilrefinery.png")
steel=PhotoImage(file="steel.png")
concrete=PhotoImage(file="concrete.png")
coal=PhotoImage(file="coal.png")
weapons=canvas.create_image(580,80, image=weap)
nur=canvas.create_image(1130,60, image=nursery)

im=canvas.create_image(70,80, image=store)


def directions():
    global direc1,direc2,direc3,direc4,direc5,direc6,direc7,direc61,direc62
    direc1=canvas.create_text(600,200, text="The goal of the game is to reduce the carbon emmitted to 0",font=('Helvetica',15))
    direc2=canvas.create_text(600,230, text="The are many combinations of ways to accomplish this",font=('Helvetica',15))
    direc3=canvas.create_text(600,260, text="The source of pollution is the 5 big polluters" ,font=('Helvetica',15))
    direc4=canvas.create_text(600,290, text="Gold coins can be collected that can be used to buy different goods at the stores. If you run out of food you lose",font=('Helvetica',15))
    direc5=canvas.create_text(600,320, text="You can buy trees to reduce the pollution, food to sustain movement or weapons to attack the polluters",font=('Helvetica',15))
    direc6=canvas.create_text(600,350, text="If you can conquer the polluters, they will no longer release carbon",font=('Helvetica',15))
    direc61=canvas.create_text(600,380, text="To collect the gold coins go over the center of them.",font=('Helvetica',15))
    direc62=canvas.create_text(600,410, text="To buy an item or to attach a polluter, go to the blue box",font=('Helvetica',15))
    direc7=canvas.create_text(600,440, text="To start the game press the space bar",font=('Helvetica',15))
    
directions()

def consume_food():
    global food
    food=food-1
    food_display.config(text="Food: "+str(food))


def buy_weapons():
    global coins,weapons
    if(coins>49):
        weapons=weapons+50
        coins=coins-50
    coins_display.config(text="Coins: "+str(coins))
    weapons_display.config(text="Weapons: "+str(weapons))
    news.config(text="You bought weapons")

def calculate_carbon():
    global carbon,steelnum,oilnum,concretenum,coalnum
    carbon=carbon-trees+steelnum+oilnum+concretenum+coalnum-trees
    carbon_display.config(text="Carbon Emmited: "+str(carbon))
   
def add_game():
    global img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12
    img1=canvas.create_image(200,600, image=img)
    img2=canvas.create_image(300,700, image=img)
    img3=canvas.create_image(1000,200, image=img)
    img4=canvas.create_image(500,700, image=img)
    img5=canvas.create_image(1000,700, image=img)
    img6=canvas.create_image(700,700, image=img)
    img7=canvas.create_image(500,100, image=img)
    img8=canvas.create_image(500,300, image=img)
    img9=canvas.create_image(800,300, image=oil)
    img10=canvas.create_image(1000,500,image=coal)
    img11=canvas.create_image(300,400, image=steel)
    img12=canvas.create_image(700,600, image=concrete)

def buy_trees():
    i=0
    global coins,trees
    news.config(text="You bought a tree")
    if((coins>9)and(trees<20)):
        trees=trees+1
        coins=coins-10
        coins_display.config(text="Coins: "+str(coins))

    if(trees>19):
        news.config(text="The nursery is sold out of plants")  

    while(i<trees):
       treee=canvas.create_image(1140,(30*i)+170, image=tree)
       i=i+1
    


def delete_instructions():
    canvas.delete(direc1)
    canvas.delete(direc2)
    canvas.delete(direc3)
    canvas.delete(direc4)
    canvas.delete(direc5)
    canvas.delete(direc6)
    canvas.delete(direc7)
    canvas.delete(direc61)
    canvas.delete(direc62)
      
    

    coins_display.config(text="Coins: "+str(coins))
    

def buy_food():
    global food,coins
    if(coins>49):
        food=food+750
        coins=coins-50
    food_display.config(text="Food: "+str(food))
    coins_display.config(text="Coins: "+str(coins))
    news.config(text="You bought Food")

def battle_steel():
    global steelnum,img11,steelwin,steellose,weapons
    outcome=random.randint(1,99)
    weapons=weapons-50
    weapons_display.config(text="Weapons: "+str(weapons))
    if(((weapons+50)/2)>=outcome):
        steelnum=0
        time.sleep(1)
        canvas.delete(img11)
        news.config(text="You elimated the steel plant")
    if(((weapons+50)/2)<outcome):
        news.config(text="You were defeated by the steel plant")
    

def battle_concrete():
    global concretenum,img12,steelwin,steellose,weapons
    outcome=random.randint(1,99)

    if((weapons/3)>=outcome):
        concretenum=0
        time.sleep(1)
        canvas.delete(img12)
        news.config(text="You elimated the concrete plant")

    if((weapons/3)<outcome):
        news.config(text="You were defeated by the concrete plant")

    weapons=weapons-50
    weapons_display.config(text="Weapons: "+str(weapons))
   

def battle_oil():
    global oilnum,img9,steelwin,steellose,weapons
    outcome=random.randint(1,99) 

    if((weapons/4)>=outcome):
        oilnum=0
        print(oilnum)
        time.sleep(1)
        canvas.delete(img9)
        news.config(text="You elimated the oil plant")
    weapons=weapons-50
    weapons_display.config(text="Weapons: "+str(weapons))

    if((weapons/4)<outcome):
        news.config(text="You were defeated by the oil plant")
          
    

def battle_coal():
    global coalnum,steelnum,img10,steelwin,steellose,weapons
    outcome=random.randint(1,99)

    if((weapons/5)>=outcome):
        coalnum=0
        time.sleep(1)
        canvas.delete(img10)
        news.config(text="You elimated the coal plant")
    weapons=weapons-50
    weapons_display.config(text="Weapons: "+str(weapons))
    if((weapons/5)<outcome):
        news.config(text="You were defeated by the coal plant")


def find_coins():
    news.config(text="You found coins")
    global coins
    coins=coins+200
    coins_display.config(text="Coins: "+str(coins))

def move_circle(event):
     
    key=event.keysym
    consume_food()

    if key=="space":
        delete_instructions()
        add_game()

           
    if ((key=="Right")and((canvas.coords(circle)[0]<1180))):
        canvas.move(circle,5,0)
                    
    if ((key=="Left") and (canvas.coords(circle)[0]>0)):
        canvas.move(circle,-5,0)
        
    if ((key=="Down")and(canvas.coords(circle)[1]<790)):
        canvas.move(circle,0,5)
                   
    if ((key=="Up")and(canvas.coords(circle)[1]>0)):
        canvas.move(circle,0,-5)

    if((canvas.coords(circle)[0]==185)&(canvas.coords(circle)[1]==585)):
        canvas.delete(img1)
        find_coins()
    if((canvas.coords(circle)[0]==285)&(canvas.coords(circle)[1]==685)):
        find_coins()
        canvas.delete(img2)
    if((canvas.coords(circle)[0]==985)&(canvas.coords(circle)[1]==185)):
       find_coins()
       canvas.delete(img3)
    if((canvas.coords(circle)[0]==485)&(canvas.coords(circle)[1]==685)):
       find_coins()
       canvas.delete(img4)
    if((canvas.coords(circle)[0]==985)&(canvas.coords(circle)[1]==685)):
       find_coins()
       canvas.delete(img5)
    if((canvas.coords(circle)[0]==685)&(canvas.coords(circle)[1]==685)):
       find_coins()
       canvas.delete(img6)
    if((canvas.coords(circle)[0]==485)&(canvas.coords(circle)[1]==85)):
       find_coins()
       canvas.delete(img7)
    if((canvas.coords(circle)[0]==485)&(canvas.coords(circle)[1]==285)):
       find_coins()
       canvas.delete(img8)

    if((canvas.coords(circle)[0]==55)&(canvas.coords(circle)[1]==135)):
       buy_food()

    if((canvas.coords(circle)[0]==560)&(canvas.coords(circle)[1]==130)):
       buy_weapons()

    if((canvas.coords(circle)[0]==1110)&(canvas.coords(circle)[1]==90)):
       buy_trees()

    if(((canvas.coords(circle)[0]==285)&(canvas.coords(circle)[1]==425))and weapons>49):
       battle_steel()

    if(((canvas.coords(circle)[0]==780)&(canvas.coords(circle)[1]==325))and weapons>49):
       battle_oil()

    if(((canvas.coords(circle)[0]==985)&(canvas.coords(circle)[1]==525))and weapons>49):
       battle_coal()

    if(((canvas.coords(circle)[0]==675)&(canvas.coords(circle)[1]==625))and weapons>49):
       battle_concrete()
    
    print(canvas.coords(circle)[0])
    print(canvas.coords(circle)[1])
    print("Hi")
                
    calculate_carbon()
    if(food<0):
        direc1rtyty=canvas.create_text(600,200, text="GAME OVER-YOU RAN OUT OF FOOD",font=('Helvetica',15))
    if(carbon<0):
        direc1rtyty=canvas.create_text(600,200, text="YOU WIN!!",font=('Helvetica',15))    
        

canvas.bind_all('<Key>',move_circle)
window.mainloop()
