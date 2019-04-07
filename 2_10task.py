import re


class calculator():
    def __add(self, num1, num2):
        return num1 + num2

    def __divide(self, num1, num2):
        return num1 / num2

    def __multiply(self, num1, num2):
        return num1 * num2

    def __subtract(self, num1, num2):
        return num1 - num2

    def calc(self, operation_name, num1, num2):
        """define which operation was received and do such operation with numbers"""
        methods_dict = {
            'add': self.__add,
            'divide': self.__divide,
            'multiply': self.__multiply,
            'subtract': self.__subtract,
        }

        try:
            result = methods_dict[operation_name](num1, num2)
            return result
        except:
            raise ValueError('This method %s is not implemented in this calculator' % operation_name)


if __name__ == '__main__':
    cl = calculator()
    num1 = int(input("a number 1 : "))
    num2 = int(input("a number 2 : "))
    operation_name = str(input("name of operation: [add, subtract, divide, multiply] : "))
    print(cl.calc(operation_name, num1, num2))
