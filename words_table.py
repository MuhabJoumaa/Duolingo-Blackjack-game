from tkinter import messagebox
from typing import Any

from model.word import Word


class WordsTable:
    words: list[Any] | Any

    def __init__(self, words=None):
        if words is None:
            words = []
        self.words = words

    def get_words(self):
        return self.words

    def add_word(self, word, translation, part_of_speech=''):
        word_object = Word(word, translation, part_of_speech)
        if word_object in self.words:
            messagebox.showerror("Ошибка", "Это слово уже существует.")
            return False
        else:
            self.words.append(word_object)
        return True

    def edit_word(self, word_index, word, translation, part_of_speech=''):
        word_object = Word(word, translation, part_of_speech)
        if word_object in self.words:
            messagebox.showerror("Ошибка", "Это слово уже существует.")
        else:
            self.words[word_index] = word_object
            messagebox.showinfo("Информация", "Слово редактировано успешно.")

    def remove_word(self, word):
        for word_object in self.words:
            if word_object.get_word() == word:
                self.words.remove(word_object)
                break
