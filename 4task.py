class LocalBuiltin():
    def __element_counting(self, element):
        result = False
        splited_list = element.split(',')
        if len(splited_list) <= 3:
            result = True
        return result

    def words_checker(self, input_list):
        filtered_words_list = [element for element in input_list if self.__element_counting(element)]
        return filtered_words_list

    def words_checker_loop(self, input_list):
        for element in input_list:
            if self.__element_counting(element):
                filtered_words_list = element
        return filtered_words_list

    def words_checker_filter(self, input_list):
        filtered_words_list = filter(self.__element_counting, input_list)
        return filtered_words_list

if __name__ == '__main__':
    lb = LocalBuiltin()
    input_list = input()
    print(lb.words_checker_filter(input_list))

