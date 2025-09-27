from model.sentences_table import SentencesTable
from model.words_table import WordsTable


class Model:
    def __init__(self, words_table: WordsTable, sentences_table: SentencesTable):
        self.words_table = words_table
        self.sentences_table = sentences_table

    def get_words_table(self):
        return self.words_table

    def get_sentences_table(self):
        return self.sentences_table
