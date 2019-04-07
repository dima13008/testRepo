class LocalBuiltin(object):
    def check_value(self, input_dict):
        result = False
        for i in input_dict:
            if type(input_dict[i]) == str:
                result = True
        return result

class LocalBuiltin_withAny(object):
    def check_value(self, input_dict):
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
    lb = LocalBuiltin()
    lba = LocalBuiltin_withAny()
    input_dict = input()
    b = lb.check_value(input_dict)
    l = lba.check_value(input_dict)
    print(b, l)
