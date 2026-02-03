class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n % 4 != 0:
                return False
            else:
                n = n//4
        if n == 1:
            return True

if __name__ == '__main__':
    s1 = Solution() 
    test = []
    for i in range(1,65):
        test.append(i)
    for i in test:
        if s1.isPowerOfFour(i):
            print(i,"is power of 4")

