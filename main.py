import tkinter
import words

# Initialize words object and load the data from files
words_obj = words.Words()


# Show word translation in English
def eng_word():
    card.itemconfig(card_title, text="English", fill="white")
    card.itemconfig(
        card_word, text=words_obj.current_word["English"], fill="white")
    card.itemconfig(card_img, image=bg_back)


# Provide new word
def handle_new_word():
    global flip_timer

    if len(words_obj.word_list) == 0:
        everything_learnt()

    window.after_cancel(flip_timer)
    words_obj.new_word()

    card.itemconfig(card_img, image=bg_front)
    card.itemconfig(card_title, text="French", fill="black")
    card.itemconfig(
        card_word, text=words_obj.current_word["French"], fill="black")

    flip_timer = window.after(3000, eng_word)


# Remove known word from list and provide new one
def is_known():
    handle_new_word()
    words_obj.remove_word()


# Handle the end of words list
def everything_learnt():
    card.itemconfig(card_img, image=bg_front)
    card.itemconfig(
        card_title, text="You've learnt all of the words", fill="black")
    card.itemconfig(
        card_word, text="Congrats!", fill="black")

    btn_wrong.grid_remove()
    btn_right.grid_remove()
    btn_restart.grid(column=1, row=1)


# Restart word list
def restart_words():
    words_obj.restart_words()

    btn_wrong.grid(column=0, row=1)
    btn_right.grid(column=2, row=1)
    btn_restart.grid_remove()

    handle_new_word()


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
card.grid(column=0, row=0, columnspan=3)


# Buttons
btn_wrong_img = tkinter.PhotoImage(file="./images/wrong.png")
btn_right_img = tkinter.PhotoImage(file="./images/right.png")

btn_wrong = tkinter.Button(
    image=btn_wrong_img, highlightthickness=0, border=0, command=handle_new_word)
btn_right = tkinter.Button(
    image=btn_right_img, highlightthickness=0, border=0, command=is_known)

btn_restart = tkinter.Button(
    text="restart", highlightthickness=0, border=0, background=BACKGROUND_COLOR, command=restart_words)

btn_wrong.grid(column=0, row=1)
btn_right.grid(column=2, row=1)

# Display the initial word
flip_timer = window.after(3000, eng_word)
handle_new_word()

# Initialize the window
window.mainloop()
