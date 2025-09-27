import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Button


class GameView:
    check_btn: Button

    def __init__(self, root, translated_words_of_sentences, other_translated_words_of_sentences, sentences,
                 translated_sentences):
        self.window = tk.Toplevel(root)
        self.window.title('Игра блекджек')
        self.translated_words_of_sentences = translated_words_of_sentences
        self.other_translated_words_of_sentences = other_translated_words_of_sentences
        self.buttons_list = []
        self.sentences = sentences
        self.translated_sentences = translated_sentences
        self.number_of_levels = len(self.sentences) - 1
        self.current_level = 1
        self.level_number = ttk.Label(self.window, text='Этап ' + str(self.current_level))
        self.level_number.pack()
        self.translate_label = ttk.Label(self.window, text='Переведите предложение')
        self.translate_label.pack()
        self.sentence_label = ttk.Label(self.window, text=self.sentences[self.current_level - 1])
        self.sentence_label.pack()
        self.translated_sentence_label = ttk.Label(self.window, text='')
        self.translated_sentence_label.pack()
        self.check_btn = ttk.Button(self.window, text='Проверить', command=self.check_answer)
        self.check_btn.pack(side='bottom')
        self.result_label = ttk.Label(self.window, text='Результат')
        self.result_label.pack(side='bottom')
        self.generate_buttons()

    def generate_buttons(self):
        for word, random_word in zip(self.translated_words_of_sentences[self.current_level - 1],
                                     self.other_translated_words_of_sentences[self.current_level - 1][:5]):
            button1 = ttk.Button(self.window, text=word,
                                 command=lambda w=word: self.output_translated_word(w))
            button1.pack(side='left', padx=15)
            button2 = ttk.Button(self.window, text=random_word,
                                 command=lambda w=random_word: self.output_translated_word(w))
            button2.pack(side='left', padx=15)
            self.buttons_list.append(button1)
            self.buttons_list.append(button2)

    def output_translated_word(self, translated_word):
        translated_sentence_label_text = self.translated_sentence_label.cget('text')
        self.translated_sentence_label.config(text=translated_sentence_label_text + ' ' + translated_word)

    def check_answer(self):
        translated_sentence = self.translated_sentence_label.cget('text')
        if self.current_level - 1 <= self.number_of_levels:
            print(translated_sentence)
            print(self.translated_sentences[self.current_level - 1])
            if translated_sentence.strip() == self.translated_sentences[self.current_level - 1]:
                self.current_level = self.current_level + 1
                self.result_label.config(text='Правильно', foreground='green')
                self.update_level()
            else:
                self.result_label.config(text='Неправильно', foreground='red')

    def update_level(self):
        if self.current_level - 1 <= self.number_of_levels:
            self.level_number.config(text='Этап ' + str(self.current_level))
            self.result_label.config(text='Результат', foreground='black')
            self.sentence_label.config(text=self.sentences[self.current_level - 1])
            self.translated_sentence_label.config(text='')
            for btn in self.buttons_list:
                btn.destroy()
            self.generate_buttons()
