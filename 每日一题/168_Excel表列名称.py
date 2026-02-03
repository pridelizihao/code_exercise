class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber > 0:
            columnNumber -= 1
            reminder = columnNumber % 26
            result = chr(ord('A')+reminder) + result
            columnNumber //= 26
        return result

if __name__ == '__main__':
    s1 = Solution()
    num1 = s1.convertToTitle(1)
    num2 = s1.convertToTitle(28)
    print('1->',num1)
    print('28->',num2)

     
