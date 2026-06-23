import random
import tkinter as tk

choices = ["rock", "paper", "scissors"]


def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"


class RockPaperScissorsGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors")
        self.resizable(True, True)
        self.minsize(320, 260)
        self.configure(bg="#222831", padx=20, pady=20)

        title_label = tk.Label(self, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#222831", fg="#00adb5")
        title_label.pack(fill=tk.X, pady=(0, 10))

        self.status_label = tk.Label(self, text="Choose rock, paper, or scissors.", font=("Arial", 12), bg="#222831", fg="#eeeeee")
        self.status_label.pack(fill=tk.X, pady=(0, 10))

        button_frame = tk.Frame(self, bg="#222831")
        button_frame.pack(fill=tk.X, pady=(0, 10))

        button_style = {
            "font": ("Arial", 11, "bold"),
            "bd": 0,
            "fg": "white",
            "activeforeground": "white",
            "relief": tk.FLAT,
            "cursor": "hand2",
        }

        style_map = {
            "rock": {"bg": "#ef233c", "activebackground": "#d90429"},
            "paper": {"bg": "#2b2d42", "activebackground": "#121629"},
            "scissors": {"bg": "#00adb5", "activebackground": "#008c99"},
        }

        for choice in choices:
            settings = {**button_style, **style_map[choice]}
            button = tk.Button(button_frame, text=choice.title(), command=lambda c=choice: self.play_round(c), **settings)
            button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        self.result_label = tk.Label(self, text="", font=("Arial", 12, "bold"), bg="#222831", fg="#ffd369")
        self.result_label.pack(fill=tk.X, pady=(10, 5))

        self.choice_label = tk.Label(self, text="", font=("Arial", 11), bg="#222831", fg="#eeeeee")
        self.choice_label.pack(fill=tk.X, pady=(0, 10))

        self.reset_button = tk.Button(self, text="Reset", width=10, command=self.reset_game, bg="#393e46", fg="white",
                                      activebackground="#00adb5", activeforeground="white", bd=0, cursor="hand2")
        self.reset_button.pack(pady=(5, 0))

    def play_round(self, player_choice):
        computer_choice = random.choice(choices)
        result = determine_winner(player_choice, computer_choice)

        self.choice_label.config(text=f"You chose: {player_choice} | Computer chose: {computer_choice}")
        self.result_label.config(text=result, fg="#ffd369")
        self.status_label.config(text="Play again or reset to clear the result.")

        if result == "It's a tie!":
            self.result_label.config(fg="#ffcc00")
        elif result == "You win!":
            self.result_label.config(fg="#7bed9f")
        elif result == "Computer wins!":
            self.result_label.config(fg="#ff0000")

    def reset_game(self):
        self.status_label.config(text="Choose rock, paper, or scissors.")
        self.result_label.config(text="")
        self.choice_label.config(text="")


if __name__ == "__main__":
    app = RockPaperScissorsGUI()
    app.mainloop()
