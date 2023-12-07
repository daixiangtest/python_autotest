import time


def test01(func):  # 定义装饰器的外部函数参数名必须定义为func
    def innfunc(*args, **kwargs):  # 内函数定义的是函数体之外的执行代码，也就是装饰器之外的功能函数名称必须为innfunc
        print("aaa")
        func(*args, **kwargs)  # func代表的是需要装饰的函数
        print("装饰器结束")

    return innfunc  # 最后返回的函数名称


def mylog(func):
    def innfunc(*args, **kwargs):
        print('日志记录...,start')
        func(*args, **kwargs)
        print('日志记录...,end')

    return innfunc


@test01
def test():
    print(11)


@mylog
def func1():
    print('功能1')


@mylog
def func2(a, b, c):
    print('功能2', a, b, c)


func1()
func2(100, 200, 300)
test()

print("*******分割线********" * 10)


# 多个装饰器
# 在函数定义阶段：执行顺序是从最靠近函数的装饰器开始，自内而外的执行
# 在函数执行阶段：执行顺序由外而内，一层层执行
def mylog1(func):
    print('mylog,start!')

    def innfunc():
        print('日志记录，start')
        func()
        print('日志记录，end')

    print('mylog,end!')
    return innfunc


def cost_time(func):
    print('cost_time,start!')
    func()

    def innfunc():
        print('开始计时')
        start = time.time()
        func()
        end = time.time()
        print(f'总共耗时:{end - start}')

    print('cost_time,end!')
    return innfunc


@mylog1
@cost_time  # 先执行cost_time→mylog的外在函数,然后先执行mylog→cost_time的内部函数
def func3():
    print('func3')
    time.sleep(3)


func3()

print("*******分割线1********" * 10)


# 带参数的装饰器的典型写法

def mylog(typ):  # 如果装饰器带参数的话需要多定义一层外函数用来接收参数
    def decorato(func):  # 第二层函数的参数用来接收函数对象
        print('外函数')

        def innfunc(*args, **kwargs):  # 定义装饰器的代码执行规则
            if typ == '文件':
                print('文件中:日志记录....')
            else:
                print('控制台:日志记录....')
            return func(*args, **kwargs)  # 返回函数对象

        return innfunc

    return decorato


@mylog('文件')
def testfunc(a, b):
    print('func2', a, b)


testfunc(10, 12)

print("*******分割线2********" * 10)


# 类装饰器

class MylogDecorator():
    def __init__(self, func):  # 通过__init__方法来构造类的属性，是装饰器作用于整个类

        self.func = func

    def __call__(self, *args, **kwargs):  # 通过__call__方法来定义装饰器的执行代码
        print('日志记录...')
        return self.func(*args, **kwargs)


@MylogDecorator
def testfunc2():
    print('func2')


testfunc2()

print("*******分割线3********" * 10)


# 缓存和计时装饰器的综合练习


class CacheDecorator:
    __cache = {}

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # 如果缓存中有对应的方法名，则直接返回对应的返回值
        if self.func.__name__ in CacheDecorator.__cache:
            return CacheDecorator.__cache[self.func.__name__]
        # 如果缓存中没有对应的方法名，则进行计算，并将结果缓存
        else:
            result = self.func(*args, **kwargs)
            CacheDecorator.__cache[self.func.__name__] = result
            return result


def cost_time(func):
    def infunc(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"耗时:{end - start}")
        return func(*args, **kwargs)

    return infunc


@cost_time
@CacheDecorator
def func1_long_time():
    """模拟耗时较长，每次执行返回结果都一样的情况"""
    print("start func1")
    time.sleep(3)
    print("end func1")
    return 999


if __name__ == '__main__':
    r1 = func1_long_time()
    r2 = func1_long_time()
    a=time.time()
    print(r1)
    print(r2)
    b=time.time()
    print(b-a)