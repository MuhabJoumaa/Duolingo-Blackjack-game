from typing import Any

from model.sentence import Sentence


class SentencesTable:
    sentences: list[Any] | Any

    def __init__(self, sentences=None):
        if sentences is None:
            sentences = []
        self.sentences = sentences

    def get_sentences(self):
        return self.sentences

    def add_sentence(self, pronoun='', verb='', adjective='', noun='', translation='', marker=None):
        sentence_object = Sentence(pronoun, verb, adjective, noun, translation, marker)
        self.sentences.append(sentence_object)

    def remove_sentence(self, sentence):
        for sentence_object in self.sentences:
            if sentence_object.get_word() == sentence:
                self.sentences.remove(sentence_object)
                break
