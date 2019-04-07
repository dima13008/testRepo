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
        if all(input_list) and all(range1):
            result = True
            min_value = self.__define_min(range1)
            max_value = self.__define_max(range1)
            for i in range(len(inputList)):
                if inputList[i] < min_value or inputList[i] > max_value:
                    result = False
            return result
        else:
            return 'invalid input values'

if __name__ == '__main__':
    lb = LocalBuiltin()
    inputList = input()
    inputRange = input()
    b = lb.rang_checker(inputList, inputRange)
    print(b)
