import math # 引入数学函数库
x1 = float(input("请输入初始值x1："))
x2 = float((input("请输入初始值x2：")))
eps = float((input("请输入精度：")))
k = 0 # k表示迭代次数
err = 1 # err表示计算得到的误差


def f1(x1, x2): # 计算函数f1的函数值
    f1 = (x1 + 3) * ((math.pow(x2, 3) - 7)) + 18
    return f1

def f2(x1, x2): # 计算函数f2的函数值
    f2 = math.sin(x2 * math.exp(x1) - 1)
    return f2

def Jacoobi(x1, x2): # 计算Jacobi矩阵
    df1_x1 = math.pow(x2, 3) - 7
    df1_x2 = (x1 + 3) * 3 * math.pow(x2, 2)
    df2_x1 = math.cos(x2 * math.exp(x1) - 1) * x2 * math.exp(x1)
    df2_x2 = math.cos(x2 * math.exp(x1) - 1) * math.exp(x1)
    J = [df1_x1, df1_x2, df2_x1, df2_x2]
    return J

def D(x1, x2): # 计算Jacobi矩阵的行列式
    J = Jacoobi(x1, x2)
    D = J[0] * J[3] - J[1] * J[2]
    return D

def error(a0, b0, a1, b1): # 误差函数
    error = math.sqrt(math.pow(a0 - a1, 2) + math.pow(b0 - b1, 2))
    return error


while err > eps: # 当计算的误差大于目标精度时，进行迭代
    k = k + 1 
    print(f"第{k}次迭代结果：")
    J = Jacoobi(x1, x2)
    D0 = D(x1, x2)
    f_1 = f1(x1, x2)
    f_2 = f2(x1, x2)
    x_1 = x1 - (J[3] * f_1 - J[1] * f_2)/D0 #计算迭代后x1的值
    x_2 = x2 - (- J[2] * f_1 + J[0] * f_2)/D0 #计算迭代后x2的值
    print(f"x1 = {x_1}")
    print(f"x2 = {x_2}")
    print(f"f1 = {f_1}, f2 = {f_2}")
    err = error(x1, x2, x_1, x_2)
    print(f"当前误差：{err}")
    x1 = x_1
    x2 = x_2
    print('-' * 20)

print(f"经过{k}次迭代后达到精度{eps}，得到近似解为：")
print(f"x1 = {x1}")
print(f"x2 = {x2}")