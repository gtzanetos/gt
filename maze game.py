from tkinter import*

window=Tk()
window.title('My First GUI')

canvas=Canvas(window, width=1000,height=700)

canvas.pack()

label=canvas.create_text(400,200,text='Welcome to the game')
label=canvas.create_text(400,220,text='Your goal is to use the arrow keys to make it to the end of the maze')
label=canvas.create_text(400,240,text='You may not cross any of the lines')

blue_rect=canvas.create_line(50,400,660,400)
blue_rect=canvas.create_line(140,400,140,350)
blue_rect=canvas.create_line(140,350,260,350)
blue_rect=canvas.create_line(260,400,260,350)

blue_rect=canvas.create_line(465,400,465,300)
blue_rect=canvas.create_line(365,400,365,350)
blue_rect=canvas.create_line(365,400,365,350)
blue_rect=canvas.create_line(365,350,465,350)
blue_rect=canvas.create_line(365,400,465,400)

blue_rect=canvas.create_line(465,300,535,300)
blue_rect=canvas.create_line(535,300,535,400)

blue_rect=canvas.create_line(660,400,660,500)
blue_rect=canvas.create_line(660,500,765,500)
blue_rect=canvas.create_line(765,500,765,400)
blue_rect=canvas.create_line(765,400,900,400)

circle=canvas.create_oval(35,370,65,400, fill='red')


def move_circle(event):
    
    key=event.keysym
    if key=="Right":
        canvas.move(circle, 25,0)
        
    if key=="Left":
        canvas.move(circle,-25,0)
        
    if ((key=="Down")):

        if((canvas.coords(circle)[0]==260)&(canvas.coords(circle)[1]<360)):
            canvas.move(circle,0,25)
            
        if((canvas.coords(circle)[0]==535)&(canvas.coords(circle)[1]<360)):
            canvas.move(circle,0,25)
            
        if((canvas.coords(circle)[0]==660)&(canvas.coords(circle)[1]<460)):
            canvas.move(circle,0,25)

        
    if (key=="Up"):

        if((canvas.coords(circle)[0]==110)&((canvas.coords(circle)[1]>330))):
            canvas.move(circle,0,-25)

        if((canvas.coords(circle)[0]==335)&((canvas.coords(circle)[1]>320))):
            canvas.move(circle,0,-25)

        if((canvas.coords(circle)[0]==435)&((canvas.coords(circle)[1]>270))):
            canvas.move(circle,0,-25)

        if((canvas.coords(circle)[0]==735)&((canvas.coords(circle)[1]>370))):
            canvas.move(circle,0,-25)
        
      
    if((canvas.coords(circle)[0]==885)&(canvas.coords(circle)[1]==370)):
        label=canvas.create_text(400,520,text='You Win!!')
     

canvas.bind_all('<Key>',move_circle)

window.mainloop()
