# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # 跳过重复节点
            else:
                current = current.next  # 移动到下一个节点
        return head

# 测试代码
def print_list(head):
    """打印链表的所有值"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def create_list(values):
    """根据值列表创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 测试用例
if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例1: [1,1,2] -> [1,2]
    list1 = create_list([1, 1, 2])
    result1 = sol.deleteDuplicates(list1)
    print("测试用例1 - 输入: [1,1,2], 输出:", print_list(result1))
    
    # 测试用例2: [1,1,2,3,3] -> [1,2,3]
    list2 = create_list([1, 1, 2, 3, 3])
    result2 = sol.deleteDuplicates(list2)
    print("测试用例2 - 输入: [1,1,2,3,3], 输出:", print_list(result2))
    
    # 测试用例3: 空链表 -> []
    list3 = create_list([])
    result3 = sol.deleteDuplicates(list3)
    print("测试用例3 - 输入: [], 输出:", print_list(result3))
    
    # 测试用例4: [1] -> [1]
    list4 = create_list([1])
    result4 = sol.deleteDuplicates(list4)
    print("测试用例4 - 输入: [1], 输出:", print_list(result4))
    
    # 测试用例5: [1,1,1] -> [1]
    list5 = create_list([1, 1, 1])
    result5 = sol.deleteDuplicates(list5)
    print("测试用例5 - 输入: [1,1,1], 输出:", print_list(result5))

