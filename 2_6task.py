import re

class typeDefiner():
    def type_definer(self, types_list):
        """Define and count all types from the list"""
        counted_types_dict = {}
        for element in types_list:
            element = re.search(r"'.*'", str(type(element)))
            if element.group() not in counted_types_dict.keys():
                counted_types_dict[element.group()] = 1
            else:
                counted_types_dict[element.group()] += 1
        return counted_types_dict

if __name__ == '__main__':
    td = typeDefiner()
    types_list = list(input("List: "))
    print(td.type_definer(types_list))

