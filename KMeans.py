#k_mean算法
import pandas as pd
import openpyxl

#参数初始化
inputfile = 'KMeansDataset10000.xlsx' #销量及其他属性数据
outputfile = 'Result.xlsx' #保存结果的文件名
k = 3 #聚类的类别
iteration = 30 #聚类最大循环次数
data = pd.read_excel(inputfile, index_col = 'id') #读取数据
data_zs = 1.0*(data - data.mean())/data.std() #数据标准化，std()表示求总体样本方差(除以n-1),numpy中std()是除以n
#print(data_zs)

from sklearn.cluster import KMeans
model = KMeans(n_clusters = k, max_iter = iteration) #分为k类
#model = KMeans(n_clusters = k, n_jobs = 4, max_iter = iteration) #分为k类，并发数4
model.fit(data_zs) #开始聚类

#简单打印结果
r1 = pd.Series(model.labels_).value_counts() #统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_) #找出聚类中心
r = pd.concat([r2, r1], axis = 1) #横向连接（0是纵向），得到聚类中心对应的类别下的数目
#print(r)
r.columns = list(data.columns) + [u'类别数目'] #重命名表头
#print(r)

#详细输出原始数据及其类别
r = pd.concat([data, pd.Series(model.labels_, index = data.index)], axis = 1)  #详细输出每个样本对应的类别
r.columns = list(data.columns) + [u'聚类类别'] #重命名表头
r.to_excel(outputfile) #保存结果

#用TSNE进行数据降维并展示聚类结果
from sklearn.manifold import TSNE
tsne = TSNE()
tsne.fit_transform(data_zs) #进行数据降维,并返回结果
tsne = pd.DataFrame(tsne.embedding_, index = data_zs.index) #转换数据格式

import matplotlib.pyplot as plt
plt.figure(figsize=(15,8))
plt.title("Approach of KMeans")
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

#不同类别用不同颜色和样式绘图
#plt.subplot(1,3,1)
d = tsne[r[u'聚类类别'] == 0]     #找出聚类类别为0的数据对应的降维结果
plt.plot(d[0], d[1], 'r.')

#plt.subplot(1,3,2)
d = tsne[r[u'聚类类别'] == 1]
plt.plot(d[0], d[1], 'go')

#plt.subplot(1,3,3)
d = tsne[r[u'聚类类别'] == 2]
plt.plot(d[0], d[1], 'b*')

'''
plt.subplot(1,3,3)
d = tsne[r[u'聚类类别'] == 3]
plt.plot(d[0], d[1], 'y+')
d = tsne[r[u'聚类类别'] == 4]
plt.plot(d[0], d[1], 'k.')
'''

plt.show()
