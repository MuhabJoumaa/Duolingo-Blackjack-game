import random
from tkinter import ttk

from model.sentence import Sentence
from model.word import Word
from view.add_sentence_window import AddSentenceWindow
from view.game_view import GameView


class AppView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.words_table = ttk.Treeview(self.root, columns=('Слово', 'Перевод', 'Часть речи'))
        self.words_table.heading('#0', text='id')
        self.words_table.column('#0', width=50)
        self.words_table.heading('#1', text='Слово')
        self.words_table.column('#1', width=100)
        self.words_table.heading('#2', text='Перевод')
        self.words_table.column('#2', width=100)
        self.words_table.heading('#3', text='Часть речи')
        self.words_table.column('#3', width=100)
        self.words_table.pack()
        self.sentences_table = ttk.Treeview(self.root, columns=('Предложение', 'Перевод', 'Маркер'))
        self.sentences_table.heading('#0', text='id')
        self.sentences_table.column('#0', width=50)
        self.sentences_table.heading('#1', text='Предложение')
        self.sentences_table.column('#1', width=200)
        self.sentences_table.heading('#2', text='Перевод')
        self.sentences_table.column('#2', width=200)
        self.sentences_table.heading('#3', text='Маркер')
        self.sentences_table.column('#3', width=100)
        self.sentences_table.pack()
        self.show_words_btn = ttk.Button(self.root, text='Показать слова')
        self.show_words_btn.pack()
        self.add_word_btn = ttk.Button(self.root, text='Добавлять слово')
        self.add_word_btn.pack()
        self.edit_word_btn = ttk.Button(self.root, text='Редактировать слово')
        self.edit_word_btn.pack()
        self.remove_word_btn = ttk.Button(self.root, text='Удалять слово')
        self.remove_word_btn.pack()
        self.add_sentence_btn = ttk.Button(self.root, text='Добавлять предложение',
                                           command=self.open_add_sentence_window)
        self.add_sentence_btn.pack()
        self.start_game_btn = ttk.Button(self.root, text='Начать игру')
        self.start_game_btn.pack()

    def get_words_table(self):
        return self.words_table

    def get_sentences_table(self):
        return self.sentences_table

    def show_words(self, words: Word):
        self.words_table.delete(*self.words_table.get_children())
        for word_object in words:
            self.words_table.insert('', 'end', text=str(len(self.words_table.get_children()) + 1), values=(
                word_object.get_word(), word_object.get_translation(), word_object.get_part_of_speech()))

    def show_sentences(self, sentences: Sentence):
        self.sentences_table.delete(*self.sentences_table.get_children())
        for sentence_object in sentences:
            self.sentences_table.insert('', 'end', text=str(len(self.sentences_table.get_children()) + 1), values=(
                sentence_object.get_sentence(), sentence_object.get_translation(), sentence_object.get_marker()))

    def open_add_sentence_window(self):
        AddSentenceWindow(self.root, self.controller)

    def start_game(self):
        rows = self.sentences_table.get_children()
        total_sentences = len(rows)
        sentences = []
        translated_sentences = []
        translated_words_of_sentences = []
        other_translated_words_of_sentences = []
        if total_sentences > 0:
            random_number_of_rows = random.randint(1, total_sentences)
            selected_number_of_rows = rows[:random_number_of_rows]
            for item in selected_number_of_rows:
                item_values = self.sentences_table.item(item)['values']
                sentence = item_values[0]
                translated_sentence = item_values[1]
                sentences.append(sentence)
                translated_sentences.append(translated_sentence)
            for sentence in sentences:
                translated_words = []
                other_translated_words = []
                for word in sentence.split():
                    for item in self.words_table.get_children():
                        i = 0
                        j = random.randint(10, 20)
                        item_values = self.words_table.item(item)['values']
                        if item_values[0] == word:
                            translated_words.append(item_values[1])
                        else:
                            if i < j:
                                other_translated_words.append((item_values[1]))
                        i + 1
                translated_words_of_sentences.append(translated_words)
                other_translated_words_of_sentences.append(other_translated_words)
            GameView(self.root, translated_words_of_sentences, other_translated_words_of_sentences, sentences,
                     translated_sentences)
