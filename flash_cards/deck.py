import pandas as pd
from flashcard import Flashcard
import random

class Deck:
    def __init__ (self,csv_file):
        self.cards=[]
        self.current_index=0
        self.load_from_csv(csv_file)
    def load_from_csv(self,file):
        df = pd.read_csv(file, header=None)
        for row in df.values:
            #row[0] is question, row[1] is answer
            new_card = Flashcard(row[0], row[1])
            self.cards.append(new_card)
    def shuffle(self):
        random.shuffle(self.cards)
        self.current_index=0
    def next_card(self):
        if self.current_index<len(self.cards)-1:
            self.current_index+=1
        else:
            self.current_index=0
    def current_card(self):
        return self.cards[self.current_index]