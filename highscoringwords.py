import operator
import random
__author__ = 'codesse'


class HighScoringWords:
    MAX_LEADERBOARD_LENGTH = 100  # the maximum number of items that can appear in the leaderboard
    MIN_WORD_LENGTH = 3  # words must be at least this many characters long
    letter_values = {}
    valid_words = []

    def __init__(self, validwords='wordlist.txt', lettervalues='letterValues.txt'):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid words, one word per line
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line
        :return:
        """
        self.leaderboard = []  # initialise an empty leaderboard
        with open(validwords) as f:
            self.valid_words = f.read().splitlines()

        with open(lettervalues) as f:
            for line in f:
                (key, val) = line.split(':')
                self.letter_values[str(key).strip().lower()] = int(val)

    def build_leaderboard_for_word_list(self):

        wordsThreeCharactersOrMore = [x for x in self.valid_words if len(x) >= 3]

        counter = 0;
        wordValues = {}
        print ""

        for word in wordsThreeCharactersOrMore:
            for letter in word:
                counter += self.letter_values[letter]
            wordValues[word] = counter;
            counter = 0;
            print ""

        sorted_words = dict(sorted(wordValues.items(), key=operator.itemgetter(1))[-100:])
        sortedValues = sorted((set([value for key, value in sorted_words.iteritems()])), reverse=True)

        for value in sortedValues:
            new_list = [k for k, v in sorted_words.items() if v == value]

            if len(new_list) == 1:
                self.leaderboard.append(new_list[0])
                continue;

            templist = sorted(new_list)
            for word in templist:
                self.leaderboard.append(word)

        print self.leaderboard


    def build_leaderboard_for_letters(self, starting_letters):

        new_word = ""
        key_len = 10




if __name__ == "__main__":
    f = HighScoringWords()
    f.__init__()
    f.build_leaderboard_for_word_list()

