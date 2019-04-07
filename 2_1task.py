class LocalBuiltin():
    def reversing_dict(self, input_dict):
        unic_dict = {}
        for key, value in input_dict.iteritems():
            if value not in unic_dict:
                unic_dict.update({value: key})
            else:
                unic_dict[value] = list(unic_dict[value]) + [key]
        return unic_dict

if __name__ == '__main__':
    lb = LocalBuiltin()
    input_list = input()
    print(lb.reversing_dict(input_list))

