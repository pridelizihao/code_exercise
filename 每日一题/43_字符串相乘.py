class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)

        # 结果数组，长度最多为 m + n
        res = [0] * (m + n)

        # 下面就是进行模拟竖式的计算
        # 从个位数开始（从右向左遍历）
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 获取当前两位的乘积
                mul = int(num1[i]) * int(num2[j])
                
                # 对应的索引位置
                p1, p2 = i + j, i + j + 1
                
                # 叠加到结果数组中（加上之前的进位/残留值）
                total = mul + res[p2]
                
                # 更新当前位和进位
                res[p2] = total % 10  # 当前位
                res[p1] += total // 10 # 进位
        
        # 将结果数组转回字符串
        # 注意：res 数组开头可能存在未使用的 0，例如 2*3=06，需要去掉前导 0
        result = "".join(map(str, res))
        
        # 如果开头是 '0' 且长度大于 1，去掉它（但这题逻辑上只会有最多一个前导0）
        return result if result[0] != '0' else result[1:]

# 测试
s = Solution()
print(s.multiply("123", "456")) # 输出 56088
