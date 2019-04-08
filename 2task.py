import doctest

class LocalBuiltin(object):
    def check_value(self, input_dict):
        """
        >>> LB = LocalBuiltin()
        >>> LB.check_value({'key1': 1, 'key2': 2})
        False
        >>> LB.check_value({'key1': '1', 'key2': 2})
        True

        """
        result = False
        for i in input_dict:
            if type(input_dict[i]) == str:
                result = True
        return result

class LocalBuiltin_withAny(object):
    def check_value(self, input_dict):
        """
        >>> LBW = LocalBuiltin_withAny()
        >>> LBW.check_value({'key1': 1, 'key2': 2})
        False
        >>> LBW.check_value({'key1': '1', 'key2': 2})
        True

        """
        listKeys = input_dict.keys()
        position = 0
        for i in input_dict:
            if type(input_dict[i]) == str:
                listKeys[position] = True
            else:
                listKeys[position] = False
            position += 1
        return any(listKeys)

if __name__ == '__main__':
    doctest.testmod()
