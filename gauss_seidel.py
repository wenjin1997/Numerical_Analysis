# Gauss Seidel迭代法
import numpy as np
import math # 引入数学函数库

A = 1. / (np.arange(1, 17) + np.arange(0, 16)[:, np.newaxis]) # 生成16阶Hilbert矩阵
b = np.array([2877/851, 3491/1431, 816/409, 2035/1187, 
            2155/1423, 538/395, 1587/1279, 573/502,
            947/895, 1669/1691, 1589/1717, 414/475,
            337/409, 905/1158, 1272/1711, 173/244])
x0 = np.array([0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
x = np.array([0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
times = 0 # 迭代次数
err = 1 # 误差

def error(x, x0): # 误差函数
    err = 0
    for i in range(len(x)):
        err = err + math.pow(x[i] - x0[i], 2)
    return err

while err > 1e-4:
    for i in range(16):
        temp = 0
        tempx = x0.copy()
        for j in range(16):
            if i != j:
                temp += x0[j] * A[i][j]
        x[i] = (b[i] - temp) / A[i][i]
        x0[i] = x[i].copy()
    err = error(x, tempx)
    times += 1
    x0 = x.copy()

print("迭代次数为：",times)
print("迭代结果为：",x)