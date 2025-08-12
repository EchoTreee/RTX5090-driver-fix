# 几何平均法
import numpy as np

# 定义判断矩阵A
A = np.array([[1, 2, 3, 5], [1/2, 1, 1/2, 2], [1/3, 2, 1, 2], [1/5, 1/2, 1/2, 1]])

# 获取A的行和列
n, _ = A.shape

# 将A中每一行元素相乘得到一列向量
prod_A = np.prod(A, axis=1)

# 将新的向量的每个分量开n次方等价求1/n次方
prod_n_A = np.power(prod_A, 1/n)

# 归一化处理
re_prod_A = prod_n_A / np.sum(prod_n_A)

# 展示权重结果
print(re_prod_A)