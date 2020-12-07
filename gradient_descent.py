# 最速下降法
import numpy as np
import math
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

while err > 1e-4:
    r = b - np.matmul(A, x0)
    a = np.inner(r, r) / np.inner(np.matmul(A, r), r) # 最优步长
    x = x0 + a * r # 计算下一个迭代点
    err = error(x, x0)
    x0 = x
    times = times + 1
    print(times, r, a, x, err)

print("迭代次数为：",times)
print("迭代结果为：",x)