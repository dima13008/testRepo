class LocalBuiltin():
    def __number_square(self, element):
        element *= element
        return element

    def words_checker(self, input_list):
        squared_list = map(self.__number_square, input_list)
        list_sum = reduce(lambda x1, x2: x1 * x2, squared_list)
        return list_sum

if __name__ == '__main__':
    lb = LocalBuiltin()
    input_list = input()
    print(lb.words_checker(input_list))

