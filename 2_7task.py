import re

class wordsSorter():
    def last_letter(self, element):
        return element[-1:]

    def last_letter_sort(self, words_list):
        """sorting list by last letter"""
        words_list.sort(key=self.last_letter)
        return words_list

if __name__ == '__main__':
    ws = wordsSorter()
    words_list = list(input("List: "))
    print(ws.last_letter_sort(words_list))

