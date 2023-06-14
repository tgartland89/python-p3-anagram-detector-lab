# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word_letters = sorted([letter for letter in word])
# this will clear pytest 1- Class Anagram in anagram.py instantiates with a single argument, a word. .
    
    def match(self, word_list):
        match_word_list = []
# this clears number two pytest, Class Anagram in anagram.py contains a method called "match"

        for word in word_list:
            if sorted([letter for letter in word]) == self.word_letters:
                      match_word_list.append (word)

        return match_word_list
# lines 11-15 will clear remaining 3 pytest 
# Class Anagram in anagram.py returns an empty list if the input list contains no words that match the initialized word. .                                                   [ 60%]
# Class Anagram in anagram.py returns a list with one element when one element of the input list matches the initialized word. .                                             [ 80%]
# Class Anagram in anagram.py returns a list with two elements when two elements of the input list match the initialized word. .
