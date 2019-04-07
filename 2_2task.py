import re

class LexemCounter():
    def reversing_dict(self, textStr):
        splittedTextList = filter(None, re.split(r'\W+', str(textStr)))
        matchflag = False
        lex_dict = {splittedTextList[0]: 0}
        for word in splittedTextList:
            for key in list(lex_dict):
                if re.match(word, key) and lex_dict.get[word] is not None:
                    lex_dict.update({word: lex_dict[word] + 1})
                    matchflag = True
                    break
            if not matchflag: lex_dict.update({word: 1})
            matchflag = False
        return lex_dict

if __name__ == '__main__':
    lb = LexemCounter()
    input_list = str(input())
    print(lb.reversing_dict(input_list))

