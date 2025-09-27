import tkinter as tk

from controller.app_controller import Controller
from model.sentences_table import SentencesTable
from model.words_table import WordsTable

root = tk.Tk()
root.title('Duolingo с блекджеком')
words_table = WordsTable()
sentences_table = SentencesTable()
controller = Controller(root, words_table, sentences_table)
root.mainloop()
