import re

class ATM():
    def ATM_dict(self, sum, cash_list):
        sum = int(sum)
        assert isinstance(cash_list, list), 'cash must be on the list'
        sorted_cash_dict = {}
        allowed_cash = [200, 100, 50, 20, 10, 1]
        for value in cash_list:
            if sum // value != 0:
                assert value in allowed_cash, "There is no selected cash in the ATM: %s" % value
                sorted_cash_dict[str(value)] = sum // value
                sum = sum - (value * sorted_cash_dict[str(value)])
            else:
                raise ValueError("Cannot split amount with given notes")

        return sorted_cash_dict

if __name__ == '__main__':
    lb = ATM()
    sum = int(input("Sum: "))
    cash_list = list(input("Cash list: "))
    print(lb.ATM_dict(sum, cash_list))

