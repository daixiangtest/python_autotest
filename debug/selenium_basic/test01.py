def month_convert(chinese):
    list1 = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二"]
    b = "00"
    for i in range(len(list1)):
        if list1[i] == chinese:
            b = "0" + str(i + 1)
    return b[-2:]


def func(c, b):
    print(c, b)
    print(b)


if __name__ == '__main__':
    a = month_convert("十")
    print(a)

# dict1 = {"aa": 1, "bb": 2}
# # print(**dict1)
# test = "我是{}sh{}".format(*dict1)
# a1, a2 = dict1.items()
#
# t1 = ("aa", "bb")
# print(dict(**{"a1": 1, "a2": 2}, c=2))
# # func(**dict1)
# # func(**dict1)
