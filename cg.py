# 共轭梯度法
import numpy as np
import math
# A = np.array([[2.0, 2], [2.0, 5]])
# b = np.array([6, 3])
# x0 = np.array([0, 0])
A = 1. / (np.arange(1, 17) + np.arange(0, 16)[:, np.newaxis]) # 生成16阶Hilbert矩阵
b = np.array([2877/851, 3491/1431, 816/409, 2035/1187, 
            2155/1423, 538/395, 1587/1279, 573/502,
            947/895, 1669/1691, 1589/1717, 414/475,
            337/409, 905/1158, 1272/1711, 173/244])
x0 = np.array([0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
times = 0 # 迭代次数
err = 1
def error(x, x0): # 误差函数
    err = 0
    for i in range(len(x)):
        err = err + math.pow(x[i] - x0[i], 2)
    return err

r_0 = b - np.matmul(A, x0)
p_0 = r_0
while err > 1e-6:
    if (np.inner(np.matmul(A, r_0), r_0) <= 1e-4) or (r_0.all() <= 1e-4):
        print("迭代结束！")
        print("迭代结果为：",x0)
        break
    else:
        a_0 = np.inner(r_0, r_0) / np.inner(np.matmul(A, r_0), r_0)
        x = x0 + a_0 * p_0
        r_1 = r_0 - a_0 * np.matmul(A, p_0)
        belta = np.inner(r_1, r_1) / np.inner(r_0, r_0)
        p_1 = r_1 + belta * p_0
        err = error(x, x0)
        r_0 = r_1
        p_0 = p_1
        x0 = x
        times = times + 1
        print("第",times,"迭代：")
        print("迭代结果为：",x0)