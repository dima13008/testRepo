import re

class wordsDefiner():
    def words_definer(self, words_row, one_letter):
        """Define all words which start with the chosen letter"""
        result = []
        words_list = list(words_row.split(" "))
        for item in words_list:
            if item.lower()[:1] == str(one_letter).lower():
                result.append(item)
        return result

if __name__ == '__main__':
    wd = wordsDefiner()
    words_row = str(input("Words: "))
    one_letter = str(input("letter: "))
    print(wd.words_definer(words_row, one_letter))

