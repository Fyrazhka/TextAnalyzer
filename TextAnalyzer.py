class TextAnalyzer (object):
    def __init__(self, text):
        frm_text = text.replace('.', ' ').replace(',', ' ').replace('!', ' ').replace('?', ' ').replace(':', ' ')
        frm_text = text.lower()
        self.text = frm_text

    def freq_all(self):
        split_text = self.text.split(' ')
        dictionary = {}
        for word in set(split_text):
            dictionary[word] = split_text.count(word)
        return dictionary

    def freq_of(self, word):
        freq_all_dict = self.freq_all()

        if word in freq_all_dict:
            return freq_all_dict[word]
        else:
            return 0
