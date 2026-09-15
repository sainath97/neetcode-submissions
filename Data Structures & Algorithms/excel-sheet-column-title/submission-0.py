class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        def number_to_letter_math(num):
            return chr(64 + ((num - 1) % 26 + 1))


        res = ''
        while (columnNumber >26):
            columnNumber, remainder = columnNumber // 26, columnNumber % 26
            res = number_to_letter_math(remainder) + res
            print ((columnNumber, remainder, res)) 
        return number_to_letter_math(columnNumber) + res
    