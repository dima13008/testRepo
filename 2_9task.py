import re

class dictSquasher():
    def squash_two_dicts(self, dict_1, dict_2):
        """squash two dicts and remove repeated symbols inside of them"""
        dict_1.update(dict_2)
        return dict_1

if __name__ == '__main__':
    lr = dictSquasher()
    dict_1 = dict(input("dict 1 : "))
    dict_2 = dict(input("dict 2 : "))
    print(lr.squash_two_dicts(dict_1, dict_2))

