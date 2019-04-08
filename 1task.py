import doctest

class LocalBuiltin(object):
    def __init__(self):
        self.inputList = []
        self.inputRange = ()

    def __define_min(self, range_list):
        min_value = 0
        for element in range_list:
            if min_value > element:
                min_value = element
        return min_value

    def __define_max(self, range_list):
        max_value = 0
        for element in range_list:
            if max_value < element:
                max_value = element
        return max_value

    def rang_checker(self, input_list, range1):
        """
        :param input_list: list
        :param range1: tuple
        :return: bool
        >>> lb = LocalBuiltin()
        >>> lb.rang_checker([1, 5, 8], (1, 9))
        True
        >>> lb.rang_checker([1, 5, 8, 11], (1, 9))
        False

        """
        if all(input_list) and all(range1):
            result = True
            min_value = self.__define_min(range1)
            max_value = self.__define_max(range1)
            for idx in range(len(input_list)):
                if input_list[idx] < min_value or input_list[idx] > max_value:
                    result = False
            return result
        else:
            return 'invalid input values'

if __name__ == '__main__':
    lb = LocalBuiltin()
    f = lb.rang_checker([1, 5, 8], (0, 9))
    print(f)
    doctest.testmod()
