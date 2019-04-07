import re

class palindromesDefiner():
    def palindrome_definer(self, row):
        """Define all palindromes in the string"""
        result = True
        start_indx = 0
        end_indx = len(row) - 1
        while start_indx != end_indx:
            if row[start_indx].lower() != row[end_indx].lower():
                result = False
                break
            start_indx += 1
            end_indx -= 1
        return result

if __name__ == '__main__':
    pd = palindromesDefiner()
    row = str(input("Row: "))
    print(pd.palindrome_definer(row))

