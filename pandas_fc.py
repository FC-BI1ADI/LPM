import numpy as np
import pandas as pd

# 表达形式
# 单列标签  'col_label'
# 多列标签  'col_label1','col_label2'...
# NAN （数值数据类型的一类数），全称 Not a Number ，表示未定义或者不可表示的值。
# axis 坐标轴, ascending 升降序

#############################################################################
# 通用事项操作
#############################################################################
# 编码格式
# utf8,gbk,gb2312,gb18030
encoding = 'utf8'
# 行列操作方向
# 按行操作 ,axis=1
# 按列操作 ,axis=0

# 转换datetime_string成为datetime类型，可以识别常见格式，若识别不了可以使用format参数指定
pd.to_datetime(datetime_string, format='%Y-%m-%d')
# 生成日期序列
pd.date_range(start='20190101', periods=5, freq='D')

# 生成随机数序列
np.random.randn(6, 4)  # 生成6*4的二维随机数array,可用于创建DataFrame

# 生成0-100，步长为5的整数array
np.random.arange(0, 100, 5)
# 生成20个，1-100中的随机数
np.random.randint(1, 100, 20)

# Series配置str组函数
pd.Series.str.lower()  # 此处仅为示例

#############################################################################
# 创建DataFrame
#############################################################################


# 创新一个dataframe
df = pd.DataFrame(np.arange(50).reshape(10, 5), columns=['a', 'b', 'c', 'd', 'e'])

# 读入剪贴板中的数据，pandas可以自动识别数据类型
df = pd.read_clipboard()

# 打开EXCEL文件
xlsx_filename = r'EXCEL文件名.xlsx'
# sheet_name 表索引
# header 第N行为header, header行 pandas会将其作为列索引
# names 指定各列的列索引
# usecols 读入指定列
df = pd.read_excel(xlsx_filename,
                   sheet_name=0,
                   header=0,
                   names=('A', 'B', 'C', ..., 'N'),
                   usecols=[0, 1, 2, ..., N])

# 利用skiprows进行数据读入抽样，首行读入，1%的抽样
df = pd.read_excel(xlsx_filename, skiprow=lambda x: x > 0 and np.random.rand() > 0.01)

# 写入EXCEL文件
df.to_excel(xlsx_filename, sheet_name=0)


# 写入多个SHEET至EXCEL文件
with pd.ExcelWriter('file_name', date_format='YYYY-MM-DD') as writer:
    df1.to_excel(writer, sheet_name='sheet1')
    df2.to_excel(writer, sheet_name='sheet2')

writer = pd.ExcelWriter("time.xlsx",  datetime_format='hh:mm:ss.000')
df.to_excel(writer, "Sheet1")
writer.close()
#############################################################################
# 查看DataFrame信息和基本操作
#############################################################################
# 查看数据的维度
df.shape
# 查看数据基本信息
df.info()
# describe 统计下数据量，标准值，平均值，最大值等
df.describe()
# 查看每一列的数据格式
df.dtypes
# 查看数据的唯一值数目
df.nunique()
# 查看空值情况
df.isnull()
# 查看df空值数量
t_df = df.copy(deep=True)
df.isnull().sum()


# pandas.DataFrame.values返回DataFrame的Numpy表示形式
df.values()
# 读取df的前几行,不指定参数默认为 5行
df.head(N)
# 读取df的后几行,不指定参数默认为 5行
df.tail(N)
# 查看df的索引
df.index
# 查看df的各列列名列表
df.columns

# 直接使用索引来选择dataframe数据，df还可以使用bool索引
# ----------------------------------------------------------------------------
df[s:e]  # 左闭右开的规则，选取指定区域行
df[s:e][col_label]  # 左闭右开的规则，选取一列
df[s:e][s:e]  # 左闭右开的规则，按位置索引选取多列
df[s:e][[col_label1, col_label2...]])  # 左闭右开的规则，按标签索引选取多列
df[bool_condition]
df[[index / list / condition], 'col_label']  # 获取指定单元格
df[[index / list / condition], [col_label1, col_label2...]]  # 获取指定行、指定列

# ----------------------------------------------------------------------------
# 以标签（行、列的名字）为索引选择数据—— df.loc[行标签,列标签]
# 以位置（第几行、第几列）为索引选择数据—— df.iloc[行位置,列位置]
# loc和iloc均可以使用切片或列表，推荐使用loc和iloc进行pandas的索引操作

# 同时根据标签和位置选择数据——df.ix[行,列],因pandas不推荐使用混合模式，尽可能使用loc和iloc方法
# 需特别注意loc取得是标签，左闭右闭，而iloc取得是位置，左闭右开
df.loc[2:4] != df.iloc[2:4]
df[2:4] == df.iloc[2:4]

# 布尔索引
df[bool condition]
df[df['col_label'] > 0]
df[df['col_label'].isin([defined list])]
#############################################################################
# DataFrame中列操作
#############################################################################
# 查看列的信息
#############################################################################
# 查看列的数据格式
df['col_label'].dtype
# 查看列的空值情况
df['col_label'].isnull()
# 查看列的唯一值
df['col_label'].unique()

# 获取列名列表
# ----------------------------------------------------------------------------
columns_list = list(df)
columns_list = list(df.columns)
columns_list = list(df.columns.values)

# 列常用操作
#############################################################################
# 设置一列为索引
df.set_index('index_col')
# 恢复默认索引
df.reset_index(drop=True)
# 去除一列的空格
df['col_label'].map(str.strip)
# 改变一列的数据类型
df['col_lablel'].astype('DATA_TYPE')
# 更改列名称
df.rename(columns={'old_col_label': 'new_col_label'}, inplace=True)
# 数据替换
df['col_label'].replace('old_content', 'new_content')

# 调整各列的顺序或是在dataframe创建过程中用columns=[col_label]指定
# ----------------------------------------------------------------------------
# 方式1：直接赋值
order = ['col_label1', 'col_label2'...]
df = df[order]
# 方式2：使用reindex方法
df = df.reindex(['col_label1', 'col_label2'...])

# 增加一列或多列
# ----------------------------------------------------------------------------
# 根据条件增加一列
df['new_col'] = np.where(df['col_label'].condition, 'true value', 'false value')
# 对DF重新索引，可以增加列标签达到添加多列的目标,fill_value不指定填充NaN
df = df.reindex(columns=[col_label1, col_label2...], fill_value='FILL VALUE')

# 删除一列或多列
# ----------------------------------------------------------------------------
df.drop('col_label', axis=1, inplace=True)
df.drop(['col_label1', 'col_label2'...], axis=1, inplace=True)
df.drop(columns=['col_label1', 'col_label2'...], inplace=True)
df.pop('col_label')
df = df.pop('col_label').to_frame()

# 将某列转为列表
df['col_label'].to_list()

# 将df中列的顺序对换
df = df[:, ::-1]

# 将df中某列的值满足一定条件，设置为新值
df.col_label[df['col_label'] > 50] = 'High'

# 转换列的类型
# ----------------------------------------------------------------------------
# 方式1：使用pd转换函数
df['col_label'] = pd.to_datetime(df['col_label'])
df['col_label'] = pd.to_timedelta(df['col_label'])
df['col_label'] = pd.to_numeric(df['col_label'])
# 方式2：使用astype强制类型转换
# dtype类型包括：float, int, bool, datetime64[ns], datetime64[ns, tz], timedelta[ns], category, object
# 默认的数据类型是: int64,float64
df['col_label'] = df['col_label'].astype('DTYPE')
# 方式3：使用自定义函数
df['col_label'] = df['col_label'].apply(user_func)

#############################################################################
# DataFrame中行操作
#############################################################################
# 获取df的行索引
row_index = list(df.index)
row_index = list(df.index.values)

# 增加一行或多行
# ----------------------------------------------------------------------------
# 以Series数据增加一行
row = pd.Series({col_label1: value1, col_label2: value2...})
df = df.append(row, ignore_index=True)
# 以新索引定位，添加一行数据
df.loc[new index] = [row data list]

# 以相同DataFrame数据增加多行
rows = df[s:e]
df = df.append(rows, ignore_index=True)

# 重新设置行索引
df = df.reset_index(drop=True)

# 行的条件索引，列条件选择行，需注意各条件做与或运算时一定要用小括号括起来
df[(df.col_label condition1) &｜(df.col_label condition2) &｜ (df.col_label conditionN)]
# 使用函数的行条件索引
df[df.col_label.isin(['str1', 'str2', 'strN'])]

# 筛选数量最多的类别
# 1.生成各类别的计数Series
counts = df.col_label.value_counts()
# 2.计算counts Series中数量最多的N个类别，取其索引，然后交给isin()函数判断
df[df.col_label.isin(counts.nlargest(N).index)]

# 删除一行或多行
# ----------------------------------------------------------------------------#
# 方式1：按行索引标签删除
df.drop(labels=[row_label_x, row_label_y], axis=0, inplace=True)
# 方式2：按行位置删除
df.drop(labels=range(s, e), axis=0, inplace=True)

# df去重
df.drop_duplicates(['col_label'])
df.drop_duplicates(subset=[col_label1, col_label2, ..., col_labelN])

# 将df中行的顺序对换
df = df[::-1, :]

#############################################################################
# 分组操作 Group
#############################################################################
# 分组，使用transform取得相同大小的列，然后在原dataframe中创建新列
new_column = df.groupby('col_label').col_label.transform('func_name')
df['col_label'] = new_column

#############################################################################
# DataFrameg整体操作
#############################################################################

# df转置
df.T
# 求df的平均值
df.mean()  # 求各列的平均值
df.mean(axis=1)  # 求各行的平均值


# df排序
df.sort_index(axis=0, ascending=True)  # 按轴排序
df.sort_values(by='col_label')

# df应用函数
df.apply(function
name)  # 只需要指定函数名
df.apply(lambda x: x + 5)  # 匿名函数

# df合并
pd.concat([df1, df2, ..., dfN], axis=0, ignore_index=True)  # 按行连接
pd.concat([df1, df2, ..., dfN]), axis = 1, ignore_index = True)  # 按列连接

pd.merge(left_df, right_df, on='KEY')

#############################################################################
# DataFrameg 显示和参数设置
#############################################################################
# 设置DataFrame显示行宽
pd.set_option('display.width', 5000)
# 设置DataFrame最大显示列数
pd.set_option('display.max_columns', 60)

pd.set_option()

# 数据分析的简便方式
# Profile a DataFrame
# 假设你拿到一个新的数据集，你不想要花费太多力气，只是想快速地探索下。那么你可以使用pandas-profiling这个模块。
# 在你的系统上安装好该模块，然后使用ProfileReport()函数，传递的参数为任何一个DataFrame。它会返回一个互动的HTML报告：
# 第一部分为该数据集的总览，以及该数据集可能出现的问题列表
# 第二部分为每一列的总结。你可以点击"toggle details"获取更多信息
# 第三部分显示列之间的关联热力图
# 第四部分为缺失值情况报告
# 第五部分显示该数据及的前几行
import pandas_profiling

pandas_profiling.ProfileReport(df)
