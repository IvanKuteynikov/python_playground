import tkinter as tk
import pandas as pd
import random
from datetime import datetime
from tkinter import messagebox
import json

BACKGROUND_COLOR = "#B1DDC6"
BACKGROUND_COLOR_FRONT = "#91C2AF"
FONT_NAME = "Arial"
DATA_FILE = "data/sr-ru.csv"

# ---------------------------- HELPER FUNCTIONS ----------------------------- #
# MOVE save_json HERE, BEFORE IT GETS CALLED
def save_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4, default=str)

# ---------------------------- LOAD WORDS ----------------------------- #
def load_dict(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        df = pd.read_csv(DATA_FILE)
        df.insert(3, "result", 0)
        df.insert(4, "times_showed", 0)
        df['last_updated'] = datetime.now()
        dict_to_learn = df.to_dict("records")
        save_json(filename, dict_to_learn)
        return dict_to_learn


current_card = {}
all_words_dict = load_dict("data/sr-ru.json")
session_list = []

def get_word():
    global current_card, all_words_dict, session_list
    show_stats()
    words_to_study = [word for word in session_list if word['result'] < 3]
    if not words_to_study:
        want_to_continue = messagebox.askyesno(title="Session Complete!", message="Want to continue?")
        if want_to_continue:
            create_session_list()
        return  # Stop the function

    current_card = random.choice(words_to_study)

    word_to_learn = current_card["Serbian"]
    canvas.itemconfig(card, image=cardback_img)
    canvas.itemconfig(card_title, text="Serbian", fill="white")
    canvas.itemconfig(definition_title, text='', fill=BACKGROUND_COLOR)
    canvas.itemconfig(card_word_to_learn, text=word_to_learn, fill="white")


def flip():
    global current_card
    definition_of_word = current_card["Definition"]
    canvas.itemconfig(card, image=cardfront_img)
    canvas.itemconfig(card_title, text="Russian", fill=BACKGROUND_COLOR)
    canvas.itemconfig(definition_title, text=definition_of_word, fill=BACKGROUND_COLOR)
    canvas.itemconfig(card_word_to_learn, text=current_card["Russian"], fill=BACKGROUND_COLOR)

# ---------------------------- FUNCTIONS ------------------------------ #

def create_session_list():
    global all_words_dict, session_list
    sorted_words = sorted(all_words_dict, key=lambda x: x['result'])
    session_list = sorted_words[:20]

def wrong_answer():
    global all_words_dict
    current_card["result"] -= 1
    current_card["times_showed"] += 1
    current_card["last_updated"] = datetime.now().isoformat()
    save_json("data/sr-ru.json", all_words_dict)
    get_word()

def right_answer():
    current_card["result"] += 1
    current_card["times_showed"] += 1
    current_card["last_updated"] = datetime.now().isoformat()
    save_json("data/sr-ru.json", all_words_dict)
    get_word()


def show_stats():
    total_words = len(all_words_dict)
    total_to_study = len([word for word in all_words_dict if word['result'] < 3])
    session_total = len(session_list)
    session_left = len([word for word in session_list if word['result'] < 3])

    stats_message = f"Session: {session_left}/{session_total} | Overall: {total_to_study}/{total_words} to learn"
    canvas.itemconfig(stats_title, text=stats_message, fill="white")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
#flip_timer = window.after(3000, flip)
canvas = tk.Canvas(width=800, height=526, highlightthickness=0)
cardback_img = tk.PhotoImage(file='images/card_back.png')
cardfront_img = tk.PhotoImage(file='images/card_front.png')
card = canvas.create_image(400, 263, image=cardback_img)
canvas.config(bg=BACKGROUND_COLOR)
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, 'italic'))
card_word_to_learn = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, 'bold'))
definition_title = canvas.create_text(400, 400, text="", font=(FONT_NAME, 16, 'italic'))
stats_title = canvas.create_text(400, 480, text="", font=(FONT_NAME, 16, 'italic'))
canvas.grid(row=0, column=0, columnspan=3)

wrong = tk.PhotoImage(file='images/wrong.png')
button_wrong = tk.Button(image=wrong, highlightthickness=0, command=wrong_answer)
button_wrong.config(bg=BACKGROUND_COLOR)
button_wrong.grid(column=0, row=1)

right = tk.PhotoImage(file='images/right.png')
button_right = tk.Button(image=right, highlightthickness=0, command=right_answer)
button_right.grid(column=2, row=1)

button_reveal = tk.Button(text="Answer", highlightthickness=0, command=flip)
button_reveal.grid(column=1, row=1)

create_session_list()
get_word()


window.mainloop()