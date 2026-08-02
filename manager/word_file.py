class WordFile:
    def __init__(self, word_kr,word_eng, meaning, image ):
        self.word_kr = word_kr
        self.word_eng = word_eng
        self.meaning = meaning
        self.image = image

    def __str__(self):
        return f'{self.word_kr} | {self.word_eng} | {self.meaning} | {self.image}'