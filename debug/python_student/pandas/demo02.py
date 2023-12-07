# import requests

list1 = [1, 2, 3, 4, 3, 22, 11, 22, 55]
hashtable = {}


# for i, j in enumerate(list1):
#     print(i, j)
#     print(hashtable)
#     print((5 - j) in hashtable)
#     if 3 - j in list1:
#         print('haha')

# 定义一个类名为aa参数列表nums和预期的值target
def aa(nums, target):
    # 声明一个空字典
    dict1 = {}
    # 使用enumerate()方法对列表进行遍历，把列表里面的值依次给到j,对应的下标给到i
    for i, j in enumerate(nums):
        # 判断当预期值减去j的值等于列表中的其中一个值则说明列表中此时的j与target-j就是我们想要的值
        if target - j in nums:
            # 把j的值赋值给字典的key,把target-j的值赋值给value
            dict1.get(j)
            dict1[j] = target - j
            break
    # 最后返回字典如果没有返回的值为空
    return dict1


if __name__ == '__main__':
    print(aa(list1, 7))
    # url = "https://develop.alpha.hamsternet.io/api/projects?query=&size=10&type=1&page=1"
    #
    # payload = {}
    # headers = {
    #
    #     'Access-Token': 'pf5lhxcNf0aHY2ihcfBicCIcr6RKUyMC1CHli6FF4FgCRTnOtg9x5bljO+dtTIx0'
    # }
    #
    # response = requests.request("GET", url, headers=headers, data=payload)
    #
    # print(response.text)
