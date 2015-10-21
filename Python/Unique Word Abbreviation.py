"""
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example: 
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
"""

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        self.dt = collections.defaultdict(set)
        for d in dictionary:
            abbr = d[0], len(d), d[-1]
            self.dt[abbr].add(d)

    def isUnique(self, word):
        abbr = word[0], len(word), word[-1]
        return self.dt[abbr] <= {word}
        


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbreviation = {}
        for word in dictionary:
            abbrev = self.buildAbbreviation(word)
            if abbrev in self.abbreviation:
                self.abbreviation[abbrev].add(word)
            else:
                self.abbreviation[abbrev] = sets.Set()
                self.abbreviation[abbrev].add(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbrev = self.buildAbbreviation(word)
        if abbrev in self.abbreviation:
            return len(self.abbreviation[abbrev]) == 1 and word in self.abbreviation[abbrev]
        else:
            return True
    
    def buildAbbreviation(self, word):
        return word if len(word) <= 2 else word[0] + str(len(word[1:-1])) + word[-1]
        