# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        anagrams = []
        sorted_word = sorted(self.word)
        
        for w in words:
            if w.lower() != self.word and sorted(w.lower()) == sorted_word:
                anagrams.append(w)
        
        return anagrams
