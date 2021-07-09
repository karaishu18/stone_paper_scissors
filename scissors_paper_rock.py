from tkinter import * 
from PIL import Image,ImageTk
from random import randint

#main window
root = Tk()
root.title("Rock Scissors Paper")
root.configure(background="#72567B")

#picture
stone_image = ImageTk.PhotoImage(Image.open("stone_user.png"))
paper_image = ImageTk.PhotoImage(Image.open("paper_user.png"))
scissors_image = ImageTk.PhotoImage(Image.open("scissors_user.png"))
stone_image_pc = ImageTk.PhotoImage(Image.open("stone_pc.png"))
paper_image_pc = ImageTk.PhotoImage(Image.open("paper_pc.png"))
scissors_image_pc = ImageTk.PhotoImage(Image.open("scissors_pc.png"))

#insert picture
user_label = Label(root,image = scissors_image,bg = "#72567B")
comp_label = Label(root,image = scissors_image_pc,bg = "#72567B")

comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores
playerScore = Label(root,text=0,font=100,bg = "#72567B",fg="White")
computerScore = Label(root,text=0,font=100,bg = "#72567B",fg="White")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicators
user_indicator = Label(root,font=50,text="USER",bg = "#72567B",fg="White")
comp_indicator = Label(root,font=50,text="COMPUTER",bg = "#72567B",fg="White")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg = Label(root,font=50,bg = "#72567B",fg="White")
msg.grid(row=3,column=2)

#update message
def updateMessage(x):
    msg['text'] = x

#update user score
def updateUserScore():
    score = int(playerScore["text"])
    score+=1
    playerScore["text"] = str(score)

#update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score+=1
    computerScore["text"] = str(score)

#checks winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "stone":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "stone":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    else:
        pass

#update choices
choices=["stone","paper","scissors"]

def updateChoice(x):       

#for users    
    if x == "stone":
        user_label.configure(image=stone_image)
    elif x == "paper":
        user_label.configure(image=paper_image)
    else:
        user_label.configure(image=scissors_image) 

#for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "stone":
       comp_label.configure(image=stone_image_pc)
    elif compChoice == "paper":
       comp_label.configure(image=paper_image_pc)  
    else: 
       comp_label.configure(image=scissors_image_pc)

    checkWin(x,compChoice)   

#buttons
stone = Button(root,width=20,height=2,text="STONE",bg="#FF3E4D",fg="white", command = lambda:updateChoice("stone")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command = lambda:updateChoice("paper")).grid(row=2,column=2)
scissors = Button(root,width=20,height=2,text="SCISSORS",bg="#0ABDE3",fg="white",command = lambda:updateChoice("scissors")).grid(row=2,column=3)

root.mainloop()