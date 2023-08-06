# -*- coding:utf-8
import pickle
import numpy as np
import time


def data_save(filepath, datasave):
    start_time = time.time()
    with open(filepath, 'wb') as f:
        pickle.dump(datasave, f)
    end_time = time.time()
    print('savedata用时：' + str(end_time - start_time) + 's')


def data_load(filepath):
    start_time = time.time()
    with open(filepath, 'rb') as f:
        dataload = pickle.load(f)
    end_time = time.time()
    print('loaddata用时：' + str(end_time - start_time) + 's')
    return dataload


if __name__ == '__main__':

    MAXNUM = 100  # 设置矩阵元素的最大值
    MINNUM = 0  # 设置矩阵元素的最小值
    ROW = 5  # 设置矩阵的行数
    COL = 4  # 设置矩阵的列数
    datasave = np.random.randint(MINNUM, MAXNUM, (ROW, COL))
    print(datasave, type(datasave))
    filepath = './binary1.txt'
    data_save(filepath, datasave)
    dataload = data_load(filepath)
    print(dataload, type(dataload))
