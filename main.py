import tkinter
from tkinter import messagebox
from functools import partial

root = tkinter.Tk()
root.title("Tic Tac Toe")
pixel = tkinter.PhotoImage(width=1, height=1)
buttons : list[tkinter.Button] = []
font = ("Arial", 25)

turn = "X"
empty_text = " "

def show_msg(title : str, msg : str):
    messagebox.showinfo(title, msg)

def reset_board():
    for x in buttons:
        x['text'] = empty_text

def button_click_event(sender : int):
    global turn
    if buttons[sender]['text'] == empty_text:
        turn = "X" if turn == "O" else "O"
        buttons[sender]['text'] = turn
        check_win()

def check_win():
    global turn
    winner = None
    count = 0
    #tie
    for x in buttons:
        if x['text'] != empty_text: count +=1
    if count == 9: winner = "tie"

    for i in range(0, 3):
        #rows
        if (buttons[i * 3]['text'] == buttons[i * 3 + 1]['text'] and
            buttons[i * 3]['text'] == buttons[i * 3 + 2]['text'] and 
            buttons[i * 3]['text'] != empty_text):
            winner = buttons[i * 3]['text'] 
        #cols
        if (buttons[i]['text'] == buttons[i + 3]['text'] and
            buttons[i]['text'] == buttons[i + 6]['text'] and 
            buttons[i]['text'] != empty_text):
            winner = buttons[i]['text'] 
        #diagonal
        if (((buttons[0]['text'] == buttons[4]['text'] and
            buttons[0]['text'] == buttons[8]['text']) or
            (buttons[2]['text'] == buttons[4]['text'] and
            buttons[2]['text'] == buttons[6]['text'])) and
            buttons[4]['text'] != empty_text):
            winner = buttons[4]['text'] 

    if winner != None:
        if winner == "tie": 
            show_msg("tie!", "the game is a tie!")
        else:
            turn = "X" if turn == "O" else "O"
            show_msg("winner!", f"{winner} won the game!")
        reset_board()

def generate_buttons():
    for button_id in range(0, 9):
        button = tkinter.Button(root, font= font, text= empty_text, image=pixel, width=100, height=100, compound="c", command=partial(
            button_click_event, button_id
        ))
        button.grid(row= button_id // 3, column= button_id % 3)
        buttons.append(button)
        print(len(buttons))

generate_buttons()
root.mainloop()