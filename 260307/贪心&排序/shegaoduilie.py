"""
每个人的身高是hi，漆面哟ki个人身高高于或等于他
现在有这样的一个peopl数组，peopl[i] = [hi, ki]
现在打乱数组，请你重新排成原来的顺序
"""

def reconstructQueue(people):
    # 先按照身高降序排序，第二排序原则是ki升序
    people.sort(key = lambda x: (-x[0],x[1]))
    res = []

    for i, p in enumerate(people):
        h, k = p[0], p[1]

        if k == i:
            res.append(p)
        elif k < i:
            # 说明前面已经有k个人身高大于或等于h了，所以直接插入到k的位置即可
            res.insert(k, p)
    return res
