from tkinter import *

from random import randint

# main window
root = Tk()
root.title("Rock Paper Scissor")
width =1000
height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.configure(bg = "black")


#============================= Image =========================================
rock_img= PhotoImage(file="images/rock.png")
paper_img= PhotoImage(file="images/paper.png") 
scissor_img= PhotoImage(file="images/scissor.png")
rock_img_comp= PhotoImage(file="images/rock_user.png")
paper_img_comp= PhotoImage(file="images/paper_user.png")
scissor_img_comp= PhotoImage(file="images/scissor_user.png")
 

##============================== Insert Pictuer =========================================
user_lable = Label(root,image=scissor_img, bg ="black")
comp_lable = Label(root,image=scissor_img_comp, bg ="black")
comp_lable.grid(row=1,column=0)
user_lable.grid(row=1,column=4)

#============================== Scores =========================================
playerScore = Label(root, text=0, font=100, bg="black", fg="white")
computerScore = Label(root, text=0, font=100, bg="black", fg="white")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)
#=============================== indicators ========================================
user_indicator = Label(root,font=50, text="USER", bg="black", fg="white" )
comp_indicator = Label(root,font=50, text="COMPUTER", bg="black", fg="white")
user_indicator.grid(row=0 ,column=3)
comp_indicator.grid(row=0,column=1)
#=============================== Messages ========================================
msg = Label(root , font=50, bg="black", fg="white")
msg.grid(row=3, column=2)
#===============================Update Messages ========================================
def updateMessage(x):
    msg['text'] = x
#===============================Update user score ========================================
def updateUserScore():
    score = int(playerScore['text'])
    score += 1
    playerScore['text']= str(score)
#===============================Update user score ========================================
def updateCompScore():
    score = int(computerScore['text'])
    score += 1
    computerScore['text']= str(score)
#===============================Check Winner ========================================
def checkWin(player,computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
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
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    else:
        pass
#=============================== For Exit ===================================== 
def ExitApp():
    root.destroy()
    exit()
#=============================== Update Choices ===================================== 
choices = ["rock","paper","scissor"]
def updateChoice(x):
#=============================== For Computer ===================================== 
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_lable.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_lable.configure(image=paper_img_comp)
    else:
        comp_lable.configure(image=scissor_img_comp)

#=============================== For User ========================================
    if x == "rock":
        user_lable.configure(image=rock_img)
    elif x == "paper":
        user_lable.configure(image=paper_img)
    else:
        user_lable.configure(image=scissor_img)
    checkWin(x,compChoice)
#=============================== Buttons ========================================

rock = Button(root, width=20, height=2, text="ROCK", bg="#ff3e4d", fg="White", command= lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#ffc40c", fg="White", command= lambda:updateChoice("paper")).grid(row=2,column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#00D9D9", fg="White", command= lambda:updateChoice("scissor")).grid(row=2,column=3)
btn_quit = Button(root, text="Quit", width=12, height=2,bg="red", fg="White", command=ExitApp)
btn_quit.grid(row=5, column=2)
#===============================METHODS========================================
# def Rock():
#     global player_choice
#     player_choice = 1
#     player_img.configure(image=rock_img)
#     MatchProcess()
 
# def Paper():
#     global player_choice
#     player_choice = 2
#     player_img.configure(image=paper_img)
#     MatchProcess()
    
# def Scissor():
#     global player_choice
#     player_choice = 3
#     player_img.configure(image=scissor_img)
#     MatchProcess()

# def MatchProcess():
#     com_choice = random.randint(1,3)
#     if com_choice == 1:
#         comp_img.configure(image=rock_comp_img)
#         ComputerRock()
#     elif com_choice == 2:
#         comp_img.configure(image=paper_comp_img)
#         ComputerPaper()
        
#     elif com_choice == 3:
#         comp_img.configure(image=scissor_comp_img)
#         CompututerScissor()

# def ComputerRock():
#     if player_choice == 1:
#         lbl_status.config(text="Game Tie")
#     elif player_choice == 2:
#         lbl_status.config(text="Player Win")
#     elif player_choice == 3:
#         lbl_status.config(text="Computer Win")
           
# def ComputerPaper():
#     if player_choice == 1:
#         lbl_status.config(text="Computer Win")
#     elif player_choice == 2:
#         lbl_status.config(text="Game Tie")
#     elif player_choice == 3:
#         lbl_status.config(text="Player Win")
    
# def CompututerScissor():
#     if player_choice == 1:
#         lbl_status.config(text="Player Win")
#     elif player_choice == 2:
#         lbl_status.config(text="Computer Win")
#     elif player_choice == 3:
#         lbl_status.config(text="Game Tie")

# def ExitApp():
#     root.destroy()
#     exit()

# #===============================LABEL WIDGET=========================================
# player_img = Label(root,image=blank_img)
# comp_img = Label(root,image=blank_img)
# lbl_player = Label(root,text="PLAYER")
# lbl_player.grid(row=1, column=1)
# lbl_player.config(bg="#99ff99")
# lbl_computer = Label(root,text="COMPUTER")
# lbl_computer.grid(row=1, column=3)
# lbl_computer.config(bg="#99ff99")
# lbl_status=Label(root, text="", font=('arial', 8))
# lbl_status.config(bg="#99ff99")
# player_img.grid(row=2,column=1, padx=30, pady=20)
# comp_img.grid(row=2,column=3, pady=20)
# lbl_status.grid(row=3, column=2)



# #===============================BUTTON WIDGET===================================
# rock = Button(root, image=sm_player_rock, command=Rock)
# paper = Button(root, image=sm_player_paper, command=Paper)
# scissor = Button(root, image=sm_player_scissor, command=Scissor)
# btn_quit = Button(root, text="Quit", command=ExitApp)
# rock.grid(row=4,column=1, pady=30)
# paper.grid(row=4,column=2, pady=30)
# scissor.grid(row=4,column=3, pady=30)
# btn_quit.grid(row=5, column=2)

# if __name__ == '__main__':
root.mainloop()