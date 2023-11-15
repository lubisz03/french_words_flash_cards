import pandas
import random


class Words:
    # Initializer
    def __init__(self):
        self.current_word = None
        self.word_list = self.words_load()

    # Load the words from files
    def words_load(self):
        try:
            data = pandas.read_csv("./data/words_to_learn.csv")
        except:
            data = pandas.read_csv("./data/french_words.csv")
            data.to_csv("./data/words_to_learn.csv", index=False)
            data = pandas.read_csv("./data/words_to_learn.csv")
            return data.to_dict(orient="records")
        else:
            return data.to_dict(orient="records")

    # Remove current word
    def remove_word(self):
        self.word_list.remove(self.current_word)
        data = pandas.DataFrame(self.word_list)
        data.to_csv("./data/words_to_learn.csv", index=False)

    # Set new current_word
    def new_word(self):
        self.current_word = random.choice(self.word_list)

    # Restart list of words
    def restart_words(self):
        data = pandas.read_csv("./data/french_words.csv")
        data.to_csv("./data/words_to_learn.csv", index=False)
        data = pandas.read_csv("./data/words_to_learn.csv")
        self.word_list = data.to_dict(orient="records")
