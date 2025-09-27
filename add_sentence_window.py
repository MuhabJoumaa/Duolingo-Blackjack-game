import tkinter as tk
from tkinter import ttk, messagebox


class AddSentenceWindow:
    templates = [
        'Мест. Гл. Прил. Сущ.',
        'Мест. Гл. Сущ.',
        'Мест. Прил.'
    ]

    def __init__(self, root, controller):
        self.controller = controller
        self.words_table = self.controller.get_app_view().get_words_table()
        self.window = tk.Toplevel(root)
        self.window.title('Добавление предложения')
        self.template_label = ttk.Label(self.window, text='Шаблон:')
        self.template_label.pack()
        self.template_entry = ttk.Combobox(self.window, values=[template for template in self.templates],
                                           width=50)
        self.template_entry.pack()
        self.template_entry.bind('<<ComboboxSelected>>', self.choose_words)
        self.pronoun_label = ttk.Label(self.window, text='Мест.:')
        self.pronoun_label.pack()
        self.pronoun_entry = ttk.Combobox(self.window, values=[], width=50)
        self.pronoun_entry.pack()
        self.pronoun_entry.bind('<<ComboboxSelected>>', self.choose_pronouns)
        self.verb_label = ttk.Label(self.window, text='Гл.:')
        self.verb_label.pack()
        self.verb_entry = ttk.Combobox(self.window, values=[], width=50)
        self.verb_entry.pack()
        self.verb_entry.bind('<<ComboboxSelected>>', self.choose_verbs)
        self.adjective_label = ttk.Label(self.window, text='Прил.:')
        self.adjective_label.pack()
        self.adjective_entry = ttk.Combobox(self.window, values=[], width=50)
        self.adjective_entry.pack()
        self.adjective_entry.bind('<<ComboboxSelected>>', self.choose_adjectives)
        self.noun_label = ttk.Label(self.window, text='Сущ.:')
        self.noun_label.pack()
        self.noun_entry = ttk.Combobox(self.window, values=[], width=50)
        self.noun_entry.pack()
        self.noun_entry.bind('<<ComboboxSelected>>', self.choose_nouns)
        self.parts_of_speech_list = [self.pronoun_entry, self.verb_entry, self.adjective_entry, self.noun_entry]
        self.all_parts_of_speech_is_selected = False
        self.translation_label = ttk.Label(self.window, text='Перевод')
        self.translation_label.pack()
        self.translation_entry = ttk.Entry(self.window, width=50)
        self.translation_entry.pack()
        self.marker_label = ttk.Label(self.window, text='Маркер:')
        self.marker_label.pack()
        self.marker_combobox = ttk.Combobox(self.window, values=['Правильно', 'Неправильно'], width=30)
        self.marker_combobox.pack()
        self.add_btn = ttk.Button(self.window, text='Добавлять', command=self.add_sentence)
        self.add_btn.pack()

    def choose_words(self, event):
        selected_template = self.template_entry.get()
        self.translation_entry.delete(0, 'end')
        if selected_template == self.templates[0]:
            self.pronoun_entry.configure(state='normal')
            self.verb_entry.configure(state='normal')
            self.adjective_entry.configure(state='normal')
            self.noun_entry.configure(state='normal')
            self.update_words_options(self.templates[0], [0, 1, 2, 3])
        elif selected_template == self.templates[1]:
            self.pronoun_entry.configure(state='normal')
            self.verb_entry.configure(state='normal')
            self.adjective_entry.configure(state='disabled')
            self.noun_entry.configure(state='normal')
            self.update_words_options(self.templates[1], [0, 1, 3])
        else:
            self.pronoun_entry.configure(state='normal')
            self.verb_entry.configure(state='disabled')
            self.adjective_entry.configure(state='normal')
            self.noun_entry.configure(state='disabled')
            self.update_words_options(self.templates[2], [0, 2])

    def choose_pronouns(self, event):
        if self.all_parts_of_speech_is_selected:
            self.translation_entry.delete(0, 'end')
            self.unselect_all_parts_of_speech()
            self.all_parts_of_speech_is_selected = False
        if self.check_all_parts_of_speech_selected():
            self.all_parts_of_speech_is_selected = True
        selected_pronoun = self.pronoun_entry.get()
        for item in self.words_table.get_children():
            item_values = self.words_table.item(item)['values']
            if item_values[0] == selected_pronoun:
                translated_pronoun = item_values[1]
                if self.translation_entry.get() == '':
                    self.translation_entry.insert('end', translated_pronoun)
                else:
                    self.translation_entry.insert('end', ' ' + translated_pronoun)

    def choose_verbs(self, event):
        if self.all_parts_of_speech_is_selected:
            self.translation_entry.delete(0, 'end')
            self.unselect_all_parts_of_speech()
            self.all_parts_of_speech_is_selected = False
        if self.check_all_parts_of_speech_selected():
            self.all_parts_of_speech_is_selected = True
        selected_verb = self.verb_entry.get()
        for item in self.words_table.get_children():
            item_values = self.words_table.item(item)['values']
            if item_values[0] == selected_verb:
                translated_verb = item_values[1]
                if self.translation_entry.get() == '':
                    self.translation_entry.insert('end', translated_verb)
                else:
                    self.translation_entry.insert('end', ' ' + translated_verb)

    def choose_adjectives(self, event):
        if self.all_parts_of_speech_is_selected:
            self.translation_entry.delete(0, 'end')
            self.unselect_all_parts_of_speech()
            self.all_parts_of_speech_is_selected = False
        if self.check_all_parts_of_speech_selected():
            self.all_parts_of_speech_is_selected = True
        selected_adjective = self.adjective_entry.get()
        for item in self.words_table.get_children():
            item_values = self.words_table.item(item)['values']
            if item_values[0] == selected_adjective:
                translated_adjective = item_values[1]
                if self.translation_entry.get() == '':
                    self.translation_entry.insert('end', translated_adjective)
                else:
                    self.translation_entry.insert('end', ' ' + translated_adjective)

    def choose_nouns(self, event):
        if self.all_parts_of_speech_is_selected:
            self.translation_entry.delete(0, 'end')
            self.unselect_all_parts_of_speech()
            self.all_parts_of_speech_is_selected = False
        if self.check_all_parts_of_speech_selected():
            self.all_parts_of_speech_is_selected = True
        selected_noun = self.noun_entry.get()
        for item in self.words_table.get_children():
            item_values = self.words_table.item(item)['values']
            if item_values[0] == selected_noun:
                translated_noun = item_values[1]
                if self.translation_entry.get() == '':
                    self.translation_entry.insert('end', translated_noun)
                else:
                    self.translation_entry.insert('end', ' ' + translated_noun)

    def update_words_options(self, part_of_speech_list, indices):
        i = 0
        for part in part_of_speech_list.split():
            words = []
            for item in self.words_table.get_children():
                item_values = self.words_table.item(item)['values']
                if item_values[2] == part:
                    words.append(item_values[0])
            self.parts_of_speech_list[indices[i]]['values'] = words
            i = i + 1

    def check_all_parts_of_speech_selected(self):
        all_parts_of_speech_selected = True
        for part in self.parts_of_speech_list:
            if part.state() != ('disabled',) and part.get() == '':
                all_parts_of_speech_selected = False
                break
        return all_parts_of_speech_selected

    def unselect_all_parts_of_speech(self):
        for part in self.parts_of_speech_list:
            part.set('')

    def add_sentence(self):
        if not self.check_all_parts_of_speech_selected() or self.marker_combobox.get() == '':
            messagebox.showerror("Ошибка", "Все поля не должны быть пустыми.")
            return
        sentence = [self.pronoun_entry.get(), self.verb_entry.get(), self.adjective_entry.get(), self.noun_entry.get(),
                    self.translation_entry.get(), self.marker_combobox.get()]
        self.controller.get_app_model().get_sentences_table().add_sentence(sentence[0], sentence[1], sentence[2],
                                                                           sentence[3],
                                                                           sentence[4], sentence[5])
        self.controller.get_app_view().show_sentences(self.controller.model.get_sentences_table().get_sentences())
        messagebox.showinfo("Информация", "Предложение добавлено успешно.")
        self.window.destroy()
