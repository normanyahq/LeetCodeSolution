class ValidWordAbbr(object):
    def abbreviate(self, word):
        if len(word) <= 2:
            return word
        else:
            return word[0] + str(len(word)-2) + word[-1]
    
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        dictionary = set(dictionary)
        self.abbr_count = dict()
        self.words = dict()
        for word in dictionary:
            abbr = self.abbreviate(word)
            self.abbr_count[abbr] = self.abbr_count.get(abbr, 0) + 1
            self.words[abbr] = word
        

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = self.abbreviate(word)
        return not self.abbr_count.get(abbr, 0) or self.abbr_count.get(abbr, 0) == 1 and word == self.words[abbr]
        


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
