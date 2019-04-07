class LocalBuiltin(object):
    def str_capitalizare(self, input_list):
        # input_list = [input_list[i].capitalize() for i in range(len(input_list)) if isinstance(input_list[i], (str, unicode))]
        cap_str_list = [element.capitalize() for element in input_list if isinstance(element, (str, unicode))]
        return cap_str_list

class LocalBuiltin_withMap(object):
    def str_capitalizare(self, input_list):
        cap_str_list = list(map(lambda x: x.capitalize() if type(x) == str else x, input_list))
        return cap_str_list

class LocalBuiltin_withLoop():
    def str_capitalizare(self, input_list):
        cap_str_list = []
        for element in input_list:
            if isinstance(element, (str, unicode)):
                cap_str_list.append(element.capitalize())
            else:
                cap_str_list.append(element)
        return cap_str_list

if __name__ == '__main__':
    lb = LocalBuiltin()
    lba = LocalBuiltin_withLoop()
    input_list = input()
    b = lb.str_capitalizare(input_list)
    l = lba.str_capitalizare(input_list)
    print(l)

