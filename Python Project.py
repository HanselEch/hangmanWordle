import tkinter as tk
import random

wordList = ["python","programming","project","hangman"]

def openHangman():
    hangWindow= tk.Toplevel(root)
    hangWindow.geometry("800x500")
    hangWindow.title("Hangman")

    label = tk.Label(hangWindow, text="Hangman!", font=('Arial', 14))
    label.pack(pady=20)

    closeButton = tk.Button(hangWindow, text="Back", command=hangWindow.destroy)
    closeButton.place(x=50,y=450)

    hEntry = tk.Entry(hangWindow)
    hEntry.place(x=350,y=410)
    label = tk.Label(hangWindow, text="Enter Your Guess!", font=('Arial', 9))
    label.place(x=310,y=380)
    
    hword = random.choice(wordList)
    hattempts = 6
    hguessed = []
    hguessedwin = []

    wordLabel= tk.Label(hangWindow, text="_ "*len(hword),font=('Arial',15))
    wordLabel.pack()

    hangCanvas=tk.Canvas(hangWindow, width=300,height=250,bg="white")
    hangCanvas.pack(pady=10,padx=10)

    hangCanvas.create_line(50,200,225,200,width=2)
    hangCanvas.create_line(75,200,75,50,width=2)
    hangCanvas.create_line(65,75,150,75,width=2)
    hangCanvas.create_line(125,75,125,90)
    
    def display():
        letter = ""
        for ch in hword:
            if ch in hguessedwin:
                letter += ch + " "
            else: 
                letter += "_ "
        wordLabel.config(text=letter)
    def checkWin():
        if (all(ch in hguessedwin for ch in hword)):
            return True
        else:
            return False
    def endGame(): 
        endWindow= tk.Toplevel(root)  
        endWindow.geometry("400x250")
        endWindow.title("Game Over")
        if(checkWin()):
            endlabel2 = tk.Label(endWindow, text="YOU WIN!\nPlease Return back to main menu")
            endlabel2.place(x=100,y=50)
        else:
            endlabel = tk.Label(endWindow, text="YOU LOST!\nThe word was: " + hword)
            endlabel.place(x=100,y=50)
        def close():
            endWindow.destroy()
            hangWindow.destroy()
        endbutton = tk.Button(endWindow, text = "Main Menu!", command = close)
        endbutton.place(x=200,y=200)
    def Error():
        errorWindow= tk.Toplevel(root)  
        errorWindow.geometry("400x250")
        errorWindow.title("ERROR!")
        errorlabel = tk.Label(errorWindow, text="Please Enter A Single Valid NON-Guessed Letter")
        errorlabel.place(x=100,y=50)
        errorbutton = tk.Button(errorWindow, text = "Exit Pop-up", command = errorWindow.destroy)
        errorbutton.place(x=200,y=200)
    def hangfigure():
        if(hattempts>=6): 
            pass
        elif(hattempts<=6 and hattempts>=5):
            hangCanvas.create_oval(115,90,135,110) 
        elif(hattempts<=5 and hattempts>=4):
            hangCanvas.create_line(125,110,125,150) 
        elif(hattempts<=4 and hattempts>=3):
            hangCanvas.create_line(125,115,105,125) 
        elif(hattempts<=3 and hattempts>=2):
            hangCanvas.create_line(125,115,145,125) 
        elif(hattempts<=2 and hattempts>=1):
            hangCanvas.create_line(125,150,110,175) 
        elif(hattempts<=1 and hattempts>=0):
            hangCanvas.create_line(125,150,140,175) 
        else:
            print("ERROR IN FIGURE")
    def hGuess():
        nonlocal hattempts
        hChar = hEntry.get().strip().lower()
        if (len(hChar) != 1 or not hChar.isalpha() or hChar in hguessed):
            Error()
        else:
            hguessed.append(hChar)
            attListLabel=tk.Label(hangWindow,text="Guessed Letters: " + str(hguessed))
            attListLabel.place(x=15,y=90)
            if hChar in hword:
                hguessedwin.append(hChar)
                attLabel=tk.Label(hangWindow,text="Correct Letter: " + hChar + "\nRemaining Attempts: " + str(hattempts))
                attLabel.place(x=15,y=40)
            else:
                hattempts -= 1
                attLabel=tk.Label(hangWindow,text="Incorrect Letter: " + hChar + "\nRemaining Attempts: " + str(hattempts))
                attLabel.place(x=15,y=40)
                hangfigure()
            display()
            if(checkWin()):
                endGame()
            elif(hattempts <= 0):
                endGame()
        hEntry.delete(0,tk.END)
  
    enterButton = tk.Button(hangWindow, text="Enter", command=hGuess)
    enterButton.place(x=470,y=410)
        

def openWordle():
    wordWindow = tk.Toplevel(root)
    wordWindow.geometry("800x500")
    wordWindow.title("Wordle")

    label = tk.Label(wordWindow, text="Wordle!", font=('Arial', 14))
    label.pack(pady=20)

    closeButton = tk.Button(wordWindow, text="Back", command=wordWindow.destroy)
    closeButton.place(x=50, y=450)
    wordList = ["codes", "snake", "lists","dunks", "dents","string"]
    word = random.choice(wordList)
    attempts = 6
    current_row = 0
    grid_frame = tk.Frame(wordWindow)
    grid_frame.pack(pady=30)
    labels = []
    for i in range(6):
        row = []
        for j in range(5):
            l = tk.Label(grid_frame, text=" ", width=4, height=2, font=('Arial', 18), borderwidth=2, relief="solid", bg="white")
            l.grid(row=i, column=j, padx=3, pady=3)
            row.append(l)
        labels.append(row)
    entry = tk.Entry(wordWindow, font=('Arial', 14))
    entry.place(x=300, y=400)

    def check_guess():
        nonlocal current_row, attempts
        guess = entry.get().strip().lower()
        if len(guess) != 5 or not guess.isalpha():
            error = tk.Toplevel(wordWindow)
            error.geometry("300x150")
            tk.Label(error, text="Please enter a 5-letter word!", font=('Arial', 10)).pack(pady=20)
            tk.Button(error, text="OK", command=error.destroy).pack()
            return
        for i, ch in enumerate(guess):
            labels[current_row][i].config(text=ch.upper())
            if ch == word[i]:
                labels[current_row][i].config(bg="green", fg="white")
            elif ch in word:
                labels[current_row][i].config(bg="gold", fg="white")
            else:
                labels[current_row][i].config(bg="gray", fg="white")
        current_row += 1
        attempts -= 1
        entry.delete(0, tk.END)
        if guess == word:
            win_popup()
        elif attempts == 0:
            lose_popup()
    def win_popup():
        win = tk.Toplevel(root)
        win.geometry("300x200")
        tk.Label(win, text="YOU WIN!\nThe word was: " + word, font=('Arial', 12)).pack(pady=20)
        tk.Button(win, text="Main Menu", command=lambda: [win.destroy(), wordWindow.destroy()]).pack()
        
    def lose_popup():
        lose = tk.Toplevel(root)
        lose.geometry("300x200")
        tk.Label(lose, text="YOU LOST!\nThe word was: " + word, font=('Arial', 12)).pack(pady=20)
        tk.Button(lose, text="Main Menu", command=lambda: [lose.destroy(), wordWindow.destroy()]).pack()

    enterButton = tk.Button(wordWindow, text="Enter", command=check_guess)
    enterButton.place(x=470, y=400)


root = tk.Tk()
root.geometry("800x500")
root.title("Main Menu")

label = tk.Label(root, text="Main Menu\nSelect one of these Options",font=('Arial', 15))
label.pack()

button = tk.Button(root, text="Select Hangman", font=('Arial', 12), command=openHangman)
button.place(x=150, y=150)
MhangCanvas=tk.Canvas(root, width=225,height=200,bg="white")
MhangCanvas.place(x=90,y=200)
MhangCanvas.create_line(50,200,225,200,width=2)
MhangCanvas.create_line(75,200,75,50,width=2)
MhangCanvas.create_line(65,75,150,75,width=2)
MhangCanvas.create_line(125,75,125,90)
MhangCanvas.create_oval(115,90,135,110) 
MhangCanvas.create_line(125,110,125,150) 
MhangCanvas.create_line(125,115,105,125) 
MhangCanvas.create_line(125,115,145,125) 
MhangCanvas.create_line(125,150,110,175) 
MhangCanvas.create_line(125,150,140,175) 

button = tk.Button(root, text="Select Wordle", font=('Arial', 12), command=openWordle)
button.place(x=450,y=150)

root.mainloop()
