print("Welcome to the kitchen")
print("Today we will be cooking one of three menu items: burger and fries, brownies or cookies")
print('You will go to the grocery store and pick out the food that you need to make the meal')
ingredients=['potatoes','burger','buns','lettuce', 'eggs','cocoa','sugar','butter','flour','chocolate chips']
ingredientscookies=['eggs','sugar','butter','flour']
answer=['g','g','g','g','g','g','g','g','g','g']
y=0
z=0

while(z==0):
    desert=input("Which one would you like to make?")
    if(desert=='cookies'):
        z=25
        x=0
        print("We are now going to choose the ingredients for cookies")
        while(x<10):
            answ=input(" Do you need "+ ingredients[x] +'? Type in y or n')
            answer[x]=answ
            if((answer[x]!='y')&(answer[x]!='n')):
                x=x-1
            x=x+1
        if((answer[4]!='y')or(answer[6]!='y')or(answer[7]!='y')or(answer[8]!='y')or(answer[9]!='y')):
           print('You will not be able to make cookies due to a missing ingredient')
           y=10

        if((answer[0]=='n')&(answer[1]=='n')&(answer[2]=='n')&(answer[3]=='n')&(answer[4]=='y')&(answer[5]=='n')&(answer[6]=='y')&(answer[7]=='y')&(answer[8]=='y')&(answer[9]=='y')):
            print('You will be able to make cookies perfectly!')
            y=10
        if(y!=10):
            print('You will be able to make cookies, but you have extra ingredients')
       


    if(desert=='brownies'):
        z=25
        x=0
        print("We are now going to choose the ingredients for brownies")
        while(x<10):
            answ=input(" Do you need "+ ingredients[x] +'? Type in y or n')
            answer[x]=answ
            if((answer[x]!='y')&(answer[x]!='n')):
                x=x-1
            x=x+1
        if((answer[4]!='y')or(answer[6]!='y')or(answer[6]!='y')or(answer[7]!='y')or(answer[8]!='y')or(answer[9]!='y')):
            print('You will not be able to make brownies due to a missing ingredient')
            y=10

        if((answer[0]=='n')&(answer[1]=='n')&(answer[2]=='n')&(answer[3]=='n')&(answer[4]=='y')&(answer[5]=='y')&(answer[6]=='y')&(answer[7]=='y')&(answer[8]=='y')&(answer[9]=='y')):
            print('You will be able to make the brownies perfectly!')
            y=10
        if(y!=10):
            print('You will be able to make cookies, but you have extra ingredients')
       


    if(desert=='burger and fries'):
        z=25
        x=0
        print("We are now going to choose the ingredients for burgers and fries")
        while(x<10):
            answ=input(" Do you need "+ ingredients[x] +'? Type in y or n')
            answer[x]=answ
            if((answer[x]!='y')&(answer[x]!='n')):
                x=x-1
            x=x+1
        if((answer[0]!='y')or(answer[1]!='y')or(answer[2]!='y')or(answer[3]!='y')):
            print('You will not be able to make burgers and fries due to a missing ingredient')
            y=10

        if((answer[0]=='y')&(answer[1]=='y')&(answer[2]=='y')&(answer[3]=='y')&(answer[4]=='n')&(answer[5]=='n')&(answer[6]=='n')&(answer[7]=='n')&(answer[8]=='n')&(answer[9]=='n')):
            print('You will be able to make the burger and fries perfectly!')
            y=10
        if(y!=10):
            print('You will be able to make burgers and fries, but you have extra ingredients')
       

print("Thank you for playing the game")
 
