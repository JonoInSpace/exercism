ALLERGENS = ['eggs','peanuts','shellfish','strawberries','tomatoes','chocolate','pollen','cats']

class Allergies:

    def __init__(self, score):
        self.score = score                
        self.allergy_lst = [x for x in ALLERGENS if self.score & 2**ALLERGENS.index(x)]

    def allergic_to(self, item):
        return item in self.allergy_lst

    @property
    def lst(self):
        return self.allergy_lst