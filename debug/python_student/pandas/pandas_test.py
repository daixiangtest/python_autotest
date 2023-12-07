import pandas as pa

# series方法可以存储整数，浮点数，字符串等数据类型
data = [1, 2, 3, 4, 5]
index = ["a", "b", "c", "d", "e"]
# 创建了一个包含data里面的数据并且将index对应的数据作为data的下标
series = pa.Series(data, index=index)
print(series)

# DataFrame方法可以将数据创建为数据库的表格形式
data = {'name': ["Alice", 'xiaohua', 'tom', 'david'],
        'Age': [15, 30, 35, 40],
        'City': ['beijing', 'shanghai', 'changsha', 'hangzhou']}

df = pa.DataFrame(data)
# 查看指定的前几行数据，默认为前5行
print(df.head(3))
print("**" * 10)
# 查看后几行数据，默认为后5行
print(df.tail(2))
print("**" * 10 + "后几行")
# 查看DataFrame的行数与列数
print(df.shape)
print("**" * 10)
# 查看DataFrame的基本统计信息
print(df.describe())
print("**" * 10)
# 通过列名查数据
print(df['name'])
print(df[['name', 'City']])  # 多个列名需要传入列表两层中括号
print("**" * 10 + '索引')
# 通过索引或行号查找行数据
print(df.loc[0])  # 通过索引
print(df.iloc[2])  # 通过行号
print("**" * 10 + '条件')
# 通过条件过滤数据
print(df[df['Age'] > 30])  # 筛选出年龄大于30的数据

"""
数据的处理
"""
# 添加新列
df['GENDER'] = ['female', 'male', 'male', 'male']
print(df)
print("**" * 10 + '新增')
# 删除列
df.drop(columns=['name'], inplace=True)
print(df)
print("**" * 10 + '排序')
# 数据排序
df.sort_values(by='Age', ascending=True, inplace=True)  # ascending升序为True反之为False
print(df)
print("**" * 10 + '合并')
# 数据合并
df1 = pa.DataFrame({'A': [1, 2, 3], 'B': [1, 2, 3]})
df2 = pa.DataFrame({'A': [2, 4, 5], 'B': [5, 4, 9], 'C': [2, 8, None]})
result = pa.concat([df1, df2])  # 对应的value值必须长度一致，没有的也要填None
print(result)
# 数据的导入与导出
# 导入csv文件的数据
df = pa.read_csv("文件名")
# 导出数据到csv文件
df.to_csv("csv文件名", index=False)
# 从Exel文件导入数据
df = pa.read_excel("文件名", sheet_name='表名')
# 导出数据至Exel
df.to_excel('文件名', index=False, sheet_name='表名')

"""
三、常用命令
以下是Pandas中常用的一些命令，涵盖了数据读取、数据处理、数据分析、数据可视化等方面的常用命令：

数据读取与写入：

pd.read_csv(): 从CSV文件读取数据。
pd.read_excel(): 从Excel文件读取数据。
pd.read_json(): 从JSON文件读取数据。
pd.read_sql(): 从数据库中读取数据。
df.to_csv(): 将数据写入到CSV文件。
df.to_excel(): 将数据写入到Excel文件。
df.to_json(): 将数据写入到JSON文件。
df.to_sql(): 将数据写入到数据库中。
数据查看与处理：

df.head(): 查看DataFrame的前几行数据。
df.tail(): 查看DataFrame的后几行数据。
df.shape: 查看DataFrame的行数和列数。
df.info(): 查看DataFrame的基本信息。
df.describe(): 查看DataFrame的基本统计信息。
df.isnull(): 检查DataFrame中的缺失值。
df.drop(): 删除指定的行或列。
df.fillna(): 填充缺失值。
df.groupby(): 按照指定的列进行分组。
df.merge(): 合并两个DataFrame。
df.sort_values(): 按照指定的列排序。
数据选择与过滤：

df['column_name']: 选择指定列。
df[['column1', 'column2']]: 选择多列。
df.loc[row_index]: 按照索引名称选择行。
df.iloc[row_number]: 按照行号选择行。
df.loc[condition]: 使用条件过滤数据。
df.query('condition'): 使用查询条件过滤数据。
数据计算与聚合：

df.mean(): 计算每列的均值。
df.sum(): 计算每列的总和。
df.min(): 计算每列的最小值。
df.max(): 计算每列的最大值。
df.count(): 计算每列的非缺失值数量。
df.groupby().aggregate(): 对分组后的数据进行聚合操作。
数据可视化：

df.plot(): 绘制DataFrame的线形图。
df.plot.bar(): 绘制DataFrame的柱状图。
df.plot.pie(): 绘制DataFrame的饼图。
df.plot.scatter(): 绘制DataFrame的散点图。
"""
