class Anagram:
    def __init__(self, listen):
        self.listen = listen
        
        
    def is_anagram(self, word):
        return sorted(word.lower()) == sorted(self.listen.lower())
    
    def match(self, words):
        return [word for word in words if self.is_anagram(word)]
    
anagram = Anagram("listen")
words = ["enlist", "silent", "google", "listen"]
print(anagram.match(words))