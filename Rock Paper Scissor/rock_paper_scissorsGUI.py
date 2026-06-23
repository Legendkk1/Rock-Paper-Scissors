import os
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
        self.minsize(360, 360)
        self.configure(bg="#222831", padx=20, pady=20)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=0)

        self.choice_images = {}
        self.load_choice_images()

        title_label = tk.Label(self, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#222831", fg="#00adb5")
        title_label.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        self.status_label = tk.Label(self, text="Choose rock, paper, or scissors.", font=("Arial", 12), bg="#222831", fg="#eeeeee")
        self.status_label.grid(row=1, column=0, sticky="ew", pady=(0, 10))

        button_frame = tk.Frame(self, bg="#222831")
        button_frame.grid(row=2, column=0, sticky="ew", pady=(0, 10))
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        button_frame.grid_columnconfigure(2, weight=1)

        button_style = {
            "font": ("Arial", 10, "bold"),
            "bd": 0,
            "fg": "white",
            "activeforeground": "white",
            "relief": tk.FLAT,
            "cursor": "hand2",
            "compound": "top",
            "padx": 8,
            "pady": 8,
        }

        style_map = {
            "rock": {"bg": "#ef233c", "activebackground": "#d90429"},
            "paper": {"bg": "#2b2d42", "activebackground": "#121629"},
            "scissors": {"bg": "#00adb5", "activebackground": "#008c99"},
        }

        for index, choice in enumerate(choices):
            image = self.choice_images.get(choice)
            settings = {**button_style, **style_map[choice]}
            if image:
                settings["image"] = image
            button = tk.Button(button_frame, text=choice.title(), command=lambda c=choice: self.play_round(c), **settings)
            if image:
                button.image = image
            button.grid(row=0, column=index, sticky="nsew", padx=5)

        computer_frame = tk.Frame(self, bg="#393e46", bd=1, relief=tk.SUNKEN)
        computer_frame.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
        computer_frame.grid_rowconfigure(1, weight=1)
        computer_frame.grid_columnconfigure(0, weight=1)

        computer_label = tk.Label(computer_frame, text="Computer Pick", font=("Arial", 12, "bold"), bg="#393e46", fg="#ffd369")
        computer_label.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 0))

        self.computer_image_label = tk.Label(computer_frame, text="No image yet", bg="#393e46", fg="#eeeeee", bd=2, relief=tk.RIDGE)
        self.computer_image_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 12, "bold"), bg="#222831", fg="#ffd369")
        self.result_label.grid(row=4, column=0, sticky="ew", pady=(10, 5))

        self.choice_label = tk.Label(self, text="", font=("Arial", 11), bg="#222831", fg="#eeeeee")
        self.choice_label.grid(row=5, column=0, sticky="ew", pady=(0, 10))

        self.reset_button = tk.Button(self, text="Reset", command=self.reset_game, bg="#393e46", fg="white",
                                      activebackground="#00adb5", activeforeground="white", bd=0, cursor="hand2")
        self.reset_button.grid(row=6, column=0, pady=(5, 0))

    def load_choice_images(self):
        # Optional image loading when you add assets to the same folder.
        # Accept both rock.png / Rock.png and similar casing.
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.choice_images = {
            "rock": None,
            "paper": None,
            "scissors": None,
        }

        file_names = {
            "rock": ["rock.png", "Rock.png"],
            "paper": ["paper.png", "Paper.png"],
            "scissors": ["scissors.png", "Scissors.png", "scissor.png", "Scissor.png"],
        }

        for choice, variants in file_names.items():
            for file_name in variants:
                file_path = os.path.join(base_dir, file_name)
                if os.path.exists(file_path):
                    try:
                        image = tk.PhotoImage(file=file_path)
                        self.choice_images[choice] = image
                        break
                    except Exception:
                        self.choice_images[choice] = None

        if not any(self.choice_images.values()):
            self.choice_images = {choice: None for choice in choices}

    def update_choice_images(self, player_choice, computer_choice):
        computer_img = self.choice_images.get(computer_choice)

        if computer_img:
            self.computer_image_label.config(image=computer_img, text="")
            self.computer_image_label.image = computer_img
        else:
            self.computer_image_label.config(image="", text=computer_choice.title() if computer_choice else "No image yet")

    def play_round(self, player_choice):
        computer_choice = random.choice(choices)
        result = determine_winner(player_choice, computer_choice)

        self.choice_label.config(text=f"You chose: {player_choice} | Computer chose: {computer_choice}")
        self.result_label.config(text=result, fg="#ffd369")
        self.status_label.config(text="Play again or reset to clear the result.")
        self.update_choice_images(player_choice, computer_choice)

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
        self.update_choice_images(None, None)


if __name__ == "__main__":
    app = RockPaperScissorsGUI()
    app.mainloop()
