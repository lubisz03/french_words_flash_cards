import tkinter
import random
import pandas

# Get all data form files
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except:
    data = pandas.read_csv("./data/french_words.csv")
    data.to_csv("./data/words_to_learn.csv", index=False)
    data = pandas.read_csv("./data/words_to_learn.csv")
    word_list = data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")


# New word and card flipping handle
current_word = None


def eng_word():
    global current_word

    card.itemconfig(card_title, text="English", fill="white")
    card.itemconfig(card_word, text=current_word["English"], fill="white")
    card.itemconfig(card_img, image=bg_back)


def new_word():
    global current_word, flip_timer

    if len(word_list) == 0:
        everything_learnt()

    window.after_cancel(flip_timer)
    current_word = random.choice(word_list)

    card.itemconfig(card_img, image=bg_front)
    card.itemconfig(card_title, text="French", fill="black")
    card.itemconfig(card_word, text=current_word["French"], fill="black")

    flip_timer = window.after(3000, eng_word)


def remove_known():
    global current_word

    word_list.remove(current_word)
    data = pandas.DataFrame(word_list)
    data.to_csv("./data/words_to_learn.csv", index=False)


def is_known():
    new_word()
    remove_known()


def everything_learnt():
    card.itemconfig(card_img, image=bg_front)
    card.itemconfig(
        card_title, text="You've learnt all of the words", fill="black")
    card.itemconfig(
        card_word, text="Congrats!", fill="black")

    btn_wrong.destroy()
    btn_right.destroy()
    btn_restart.grid(column=0, row=1)


def restart_words():
    global word_list

    data = pandas.read_csv("./data/french_words.csv")
    data.to_csv("./data/words_to_learn.csv", index=False)
    data = pandas.read_csv("./data/words_to_learn.csv")
    word_list = data.to_dict(orient="records")

    btn_wrong = tkinter.Button(
        image=btn_wrong_img, highlightthickness=0, border=0, command=new_word)
    btn_right = tkinter.Button(
        image=btn_right_img, highlightthickness=0, border=0, command=is_known)

    btn_wrong.grid(column=0, row=1)
    btn_right.grid(column=1, row=1)
    btn_restart.destroy()

    new_word()


# Set up the window
BACKGROUND_COLOR = "#B1DDC6"

window = tkinter.Tk()
window.title("Flashy")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

# Set up the flash card
card = tkinter.Canvas(height=526, width=800)
bg_front = tkinter.PhotoImage(file="./images/card_front.png")
bg_back = tkinter.PhotoImage(file="./images/card_back.png")

card_img = card.create_image(400, 263, image=bg_front)
card_title = card.create_text(400, 150, text="Title", font=(
    "Ariel", 40, "italic"), fill="black")
card_word = card.create_text(400, 263, text="word", font=(
    "Ariel", 60, "bold"), fill="black")

card.config(highlightthickness=0, bg=BACKGROUND_COLOR)
card.grid(column=0, row=0, columnspan=2)


# Buttons
btn_wrong_img = tkinter.PhotoImage(file="./images/wrong.png")
btn_right_img = tkinter.PhotoImage(file="./images/right.png")

btn_wrong = tkinter.Button(
    image=btn_wrong_img, highlightthickness=0, border=0, command=new_word)
btn_right = tkinter.Button(
    image=btn_right_img, highlightthickness=0, border=0, command=is_known)

btn_restart = tkinter.Button(
    text="restart", highlightthickness=0, border=0, background=BACKGROUND_COLOR, command=restart_words)

btn_wrong.grid(column=0, row=1)
btn_right.grid(column=1, row=1)

# Display the initial word
flip_timer = window.after(3000, eng_word)
new_word()

# Initialize the window
window.mainloop()
