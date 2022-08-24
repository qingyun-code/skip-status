import torch
import loss_function as LF
import dataset as D
import net as N
from torch.utils.data import Dataset, DataLoader

# 设置迭代次数
epoch = 10

# 设置批量的大小
batch_size = 10

# 设置学习率
lr = 0.01

# 加载数据
train_data = D.dataset(is_train = True)
data = DataLoader(train_data, batch_size = batch_size, shuffle = True)

# 初始化一个网络对象
net = N.net().cuda()

# 初始化优化器
optimizer = torch.optim.SGD(net.parameters(), lr = lr, momentum = 0.9, weight_decay = 0.0005)

# 进行迭代训练
for e in range(epoch):
	for i, (inputs, labels) in enumerate(data):
		inputs = inputs.float().cuda()
		labels = labels.float().cuda()
		predict = net(inputs)
		loss = LF.loss_function(predict, labels)
		print("epoch={},i={},loss={}".format(e, i, str(loss)))
		optimizer.zero_grad()
		loss.backward()
		optimizer.step()

	# 存储模型
	torch.save(net, "weight/weight.pkl")