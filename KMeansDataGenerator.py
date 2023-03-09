import numpy as np
import pandas as pd
import openpyxl

line_count = [1000, 10000, 100000, 200000]  # 生成100行数据

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

    df = pd.DataFrame(data_dict)
    df.to_excel('KMeansDataset'+str(item)+'.xlsx', index=False)

    data_dict['id'].clear()
    data_dict['fre'].clear()
    data_dict['cost_even'].clear()
