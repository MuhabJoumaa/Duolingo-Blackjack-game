class Sentence:
    def __init__(self, pronoun='', verb='', adjective='', noun='', translation='', marker=None):
        self.pronoun = pronoun
        self.verb = verb
        self.adjective = adjective
        self.noun = noun
        self.translation = translation
        self.marker = marker

    def get_pronoun(self):
        return self.pronoun

    def get_verb(self):
        return self.verb

    def get_adjective(self):
        return self.adjective

    def get_noun(self):
        return self.noun

    def get_sentence(self):
        return self.get_pronoun() + ' ' + self.get_verb() + ' ' + self.get_adjective() + ' ' + self.get_noun()

    def get_translation(self):
        return self.translation

    def set_translation(self, translation):
        self.translation = translation

    def get_marker(self):
        return self.marker

    def set_marker(self, marker):
        self.marker = marker
