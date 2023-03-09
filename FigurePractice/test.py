import numpy as np
import pandas as pd
import openpyxl

line_count = [3, 4, 5, 6]  # 生成100行数据

data_id = []
data_fre = []
data_costeven = []
data_dict = {'id': data_id, 'fre': data_fre, 'cost_even': data_costeven}

print("初始消费数据表", data_dict)

for item in line_count:
    for i in range(0, item):
        id = i
        fre = np.random.random()
        cost = np.random.uniform(1, 3000)

        data_id.append(id)
        data_fre.append(fre)
        data_costeven.append(cost)

    print(item)
    print(data_dict['id'])
    data_dict['id'].clear()
    print(data_dict['id'])

da = [0, 1, 2, 3, 4, 5]
d = {'id': da}
print('d ---> ',d)

da.remove(1)
print('d ---> ',d,'da ---> ', da)
