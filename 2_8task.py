import re

class listReplacer():
    def replace_element_in_lists(self, words_list_1, words_list_2, element):
        """put chosen element into the 2nd list saving a position"""
        if element in words_list_1:
            position = words_list_1.index(element)
            del words_list_1[position]
            words_list_2.insert(position, element)
        else:
            raise ValueError("There is no selected element")
        return words_list_2

if __name__ == '__main__':
    lr = listReplacer()
    words_list_1= list(input("List with element: "))
    words_list_2 = list(input("List without element: "))
    element = int(input("Element: "))
    print(lr.replace_element_in_lists(words_list_1, words_list_2, element))

