import tkinter as tk
from tkinter import ttk, messagebox


class AddAndEditWordWindow:
    parts_of_speech = ['Мест.', 'Гл.', 'Прил.', 'Сущ.']

    def __init__(self, root, controller, add_or_edit, selected_word=None):
        self.controller = controller
        self.model = self.controller.get_app_model()
        self.view = self.controller.get_app_view()
        self.add_or_edit = add_or_edit
        self.words_table = self.controller.get_app_view().get_words_table()
        self.window = tk.Toplevel(root)
        self.window.title('Добавление слова' if self.add_or_edit else 'Редактирование слова')
        self.word_label = ttk.Label(self.window, text='Слово:')
        self.word_label.pack()
        self.word_entry = ttk.Entry(self.window, width=50)
        self.word_entry.insert(0,
                               '' if self.add_or_edit else self.words_table.item(selected_word)['values'][0])
        self.word_entry.pack()
        self.translation_label = ttk.Label(self.window, text='Перевод слова:')
        self.translation_label.pack()
        self.translation_entry = ttk.Entry(self.window, width=50)
        self.translation_entry.insert(0,
                                      '' if self.add_or_edit else
                                      self.words_table.item(selected_word)['values'][1])
        self.translation_entry.pack()
        self.part_of_speech_label = ttk.Label(self.window, text='Часть речи:')
        self.part_of_speech_label.pack()
        self.part_of_speech_entry = ttk.Combobox(self.window,
                                                 values=[part_of_speech for part_of_speech in self.parts_of_speech],
                                                 width=50)
        self.part_of_speech_entry.current(
            0 if self.add_or_edit else self.parts_of_speech.index(self.words_table.item(selected_word)['values'][2]))
        self.part_of_speech_entry.pack()
        self.add_edit_btn = ttk.Button(self.window, text='Добавлять' if self.add_or_edit else 'Редактировать',
                                       command=self.add_edit_word)
        self.add_edit_btn.pack()

    def check_all_fields_selected(self):
        if self.word_entry.get() == '' or self.translation_entry.get() == '':
            return False
        return True

    def add_edit_word(self):
        if not self.check_all_fields_selected():
            messagebox.showerror("Ошибка", "Поля слова и перевода не должны быть пустыми.")
            return
        english_word = self.word_entry.get()
        russian_translation = self.translation_entry.get()
        part_of_speech = self.part_of_speech_entry.get()
        if self.add_or_edit:
            status = self.model.get_words_table().add_word(english_word, russian_translation, part_of_speech)
            if status:
                self.view.show_words(self.model.get_words_table().get_words())
                messagebox.showinfo("Информация", "Слово добавлено успешно.")
        else:
            selected_word = self.view.words_table.focus()
            if selected_word:
                word_id = self.view.words_table.item(selected_word)['text']
                self.model.get_words_table().edit_word(int(word_id) - 1, english_word, russian_translation,
                                                       part_of_speech)
                self.view.show_words(self.model.get_words_table().get_words())
        self.window.destroy()
