import tkinter as tk
import random

def play(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    player_label.config(text="Your choice: " + player_choice)
    computer_label.config(text="Computer's choice: " + computer_choice)
    
    if player_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text="You win!")
    else:
        result_label.config(text="You lose!")


root = tk.Tk()
root.title("Rock Paper Scissors")


player_label = tk.Label(root, text="Your choice: ", font=("Arial", 12))
player_label.pack()

computer_label = tk.Label(root, text="Computer's choice: ", font=("Arial", 12))
computer_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack()


choices = ["Rock", "Paper", "Scissors"]
for choice in choices:
    btn = tk.Button(root, text=choice, font=("Arial", 12), padx=20, pady=10,
                    command=lambda ch=choice: play(ch))
    btn.pack(pady=5)

root.mainloop()
