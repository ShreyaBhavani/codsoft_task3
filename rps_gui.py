import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("350x400")
root.configure(bg="#add8e6") 
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["rock", "paper", "scissors"])

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Your Score: {user_score}    |    Computer Score: {computer_score}")

def reset():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text="Your Score: 0    |    Computer Score: 0")

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 18, "bold"), bg="#add8e6", fg="#003366")
title_label.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#add8e6", fg="#222", justify="center")
result_label.pack(pady=20)

score_label = tk.Label(root, text="Your Score: 0    |    Computer Score: 0", font=("Arial", 12, "bold"), bg="#add8e6", fg="#003366")
score_label.pack(pady=10)


button_frame = tk.Frame(root, bg="#add8e6")
button_frame.pack(pady=20)


button_color = "#d3d3d3" 


rock_btn = tk.Button(button_frame, text="🪨 Rock", font=("Arial", 12), width=12, bg=button_color, command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=10)


paper_btn = tk.Button(button_frame, text="📄 Paper", font=("Arial", 12), width=12, bg=button_color, command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=10)


scissors_btn = tk.Button(button_frame, text="✂️ Scissors", font=("Arial", 12), width=12, bg=button_color, command=lambda: play("scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

reset_btn = tk.Button(root, text="🔄 Reset Game", font=("Arial", 11), bg="#003366", fg="white", width=20, command=reset)
reset_btn.pack(pady=20)

root.mainloop()
