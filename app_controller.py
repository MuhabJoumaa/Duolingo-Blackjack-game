from tkinter import messagebox

from model.app_model import Model
from model.sentences_table import SentencesTable
from model.words_table import WordsTable
from view.add_edit_word_window import AddAndEditWordWindow
from view.app_view import AppView
from words_generator import WordsGenerator


class Controller:
    def __init__(self, root, words_table: WordsTable, sentences_table: SentencesTable):
        self.model = Model(words_table, sentences_table)
        self.root = root
        self.view = AppView(self.root, self)
        self.view.show_words_btn.bind('<Button-1>', self.show_words)
        self.view.add_word_btn.bind('<Button-1>', self.add_word)
        self.view.edit_word_btn.bind('<Button-1>', self.edit_word)
        self.view.remove_word_btn.bind('<Button-1>', self.remove_word)
        self.view.start_game_btn.bind('<Button-1>', self.start_game)
        self.view.get_sentences_table().bind('<<TreeviewSelect>>', self.change_marker)
        self.view.show_words(self.model.get_words_table().get_words())
        self.view.show_sentences(self.model.get_sentences_table().get_sentences())

    def get_app_view(self):
        return self.view

    def get_app_model(self):
        return self.model

    def show_words(self, event):
        for word_tuple in WordsGenerator.generate_words():
            english_word = word_tuple[0]
            russian_translation = word_tuple[1]
            part_of_speech = word_tuple[2]
            self.model.get_words_table().add_word(english_word, russian_translation, part_of_speech)
        self.view.show_words(self.model.get_words_table().get_words())

    def add_word(self, event):
        AddAndEditWordWindow(self.root, self, True)

    def edit_word(self, event):
        selected_word = self.view.words_table.focus()
        if selected_word:
            AddAndEditWordWindow(self.root, self, False, selected_word)
        else:
            messagebox.showerror("Ошибка", "Слово не выбрано.")

    def remove_word(self, event):
        selected_word = self.view.words_table.focus()
        if selected_word:
            word_id = self.view.words_table.item(selected_word)['text']
            word = self.model.get_words_table().get_words()[int(word_id) - 1]
            self.model.get_words_table().remove_word(word.get_word())
            self.view.show_words(self.model.get_words_table().get_words())

    def change_marker(self, event):
        selected_marker = self.view.sentences_table.focus()
        current_values = self.view.sentences_table.item(selected_marker)['values']
        current_marker = current_values[2]
        new_marker = 'Неправильно' if current_marker == 'Правильно' else 'Правильно'
        self.view.sentences_table.item(selected_marker, values=(current_values[0], current_values[1], new_marker))

    def start_game(self, event):
        self.view.start_game()
